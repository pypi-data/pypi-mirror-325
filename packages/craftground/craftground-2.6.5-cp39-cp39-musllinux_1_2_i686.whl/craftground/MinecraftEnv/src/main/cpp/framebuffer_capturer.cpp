#include <jni.h>
#ifdef __APPLE__
#define GL_SILENCE_DEPRECATION
#include "framebuffer_capturer_apple.h"
#include <OpenGL/OpenGL.h>
// #include <OpenGL/gl.h>
#include <OpenGL/gl3.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#else
//    #include <GL/gl.h>
#include <GL/glew.h>
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
#endif

#include <cstring> // For strcmp
#include <iostream>

#ifdef HAS_PNG
#include <png.h>
#endif
#include <stdlib.h>
#include <vector>

#define GL_PACK_REVERSE_ROW_ORDER_ANGLE 0x93A4 // extension

// https://gist.github.com/dobrokot/10486786
typedef unsigned char ui8;
#define ASSERT_EX(cond, error_message)                                         \
    do {                                                                       \
        if (!(cond)) {                                                         \
            std::cerr << error_message;                                        \
            exit(1);                                                           \
        }                                                                      \
    } while (0)

#ifdef HAS_PNG
static void
PngWriteCallback(png_structp png_ptr, png_bytep data, png_size_t length) {
    std::vector<ui8> *p = (std::vector<ui8> *)png_get_io_ptr(png_ptr);
    p->insert(p->end(), data, data + length);
}

struct TPngDestructor {
    png_struct *p;
    TPngDestructor(png_struct *p) : p(p) {}
    ~TPngDestructor() {
        if (p) {
            png_destroy_write_struct(&p, NULL);
        }
    }
};

void WritePngToMemory(
    size_t w, size_t h, const ui8 *dataRGB, std::vector<ui8> &out
) {
    out.clear();
    png_structp p =
        png_create_write_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    ASSERT_EX(p, "png_create_write_struct() failed");
    TPngDestructor destroyPng(p);
    png_infop info_ptr = png_create_info_struct(p);
    ASSERT_EX(info_ptr, "png_create_info_struct() failed");
    ASSERT_EX(0 == setjmp(png_jmpbuf(p)), "setjmp(png_jmpbuf(p) failed");
    png_set_IHDR(
        p,
        info_ptr,
        w,
        h,
        8,
        PNG_COLOR_TYPE_RGB,
        PNG_INTERLACE_NONE,
        PNG_COMPRESSION_TYPE_DEFAULT,
        PNG_FILTER_TYPE_DEFAULT
    );
    // png_set_compression_level(p, 1);
    std::vector<ui8 *> rows(h);
    for (size_t y = 0; y < h; ++y)
        rows[y] = (ui8 *)dataRGB + y * w * 3;
    png_set_rows(p, info_ptr, &rows[0]);
    png_set_write_fn(p, &out, PngWriteCallback, NULL);
    png_write_png(p, info_ptr, PNG_TRANSFORM_IDENTITY, NULL);
}
#endif

// FIXME: Use glGetIntegerv(GL_NUM_EXTENSIONS) then use glGetStringi for
// OpenGL 3.0+
bool isExtensionSupported(const char *extName) {
    // Get the list of supported extensions
    const char *extensions =
        reinterpret_cast<const char *>(glGetString(GL_EXTENSIONS));
    // FIXME: It returns nullptr after OpenGL 3.0+, even if there are extensions
    // Check for NULL pointer (just in case no OpenGL context is active)
    if (extensions == nullptr) {
        std::cerr
            << "Could not get OpenGL extensions list. Make sure an OpenGL "
               "context is active."
            << std::endl;
        return false;
    }

    // Search for the extension in the list
    const char *start = extensions;
    const char *where;
    const char *terminator;

    // Extension names should not have spaces
    while ((where = strchr(start, ' ')) || (where = strchr(start, '\0'))) {
        terminator = where;
        if ((terminator - start) == strlen(extName) &&
            strncmp(start, extName, terminator - start) == 0) {
            // Found the extension
            return true;
        }
        if (*where == '\0') {
            break; // Reached the end of the list
        }
        start = where + 1; // Move past the space
    }

    // Extension not found
    return false;
}

extern "C" JNIEXPORT jboolean JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_checkExtension(
    JNIEnv *env, jclass clazz
) {
    // Check for the GL_ARB_pixel_buffer_object extension
    return (jboolean)isExtensionSupported("GL_ANGLE_pack_reverse_row_order");
}

extern "C" JNIEXPORT jboolean JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_initializeGLEW(
    JNIEnv *env, jclass clazz
) {
#ifdef __APPLE__
    return true;
#else
    glewExperimental = GL_TRUE;
    GLenum err = glewInit();
    if (err != GLEW_OK) {
        std::cerr << "GLEW initialization failed: " << glewGetErrorString(err)
                  << std::endl;
    }
    return err == GLEW_OK;
#endif
}

enum EncodingMode { RAW = 0, PNG = 1, ZEROCOPY = 2 };

// 16 x 16 bitmap cursor
// 0: transparent, 1: white, 2: black
// https://github.com/openai/Video-Pre-Training/blob/main/cursors/mouse_cursor_white_16x16.png
// MIT License
const GLubyte cursor[16][16] = {
    {2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},

    {2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0},

    {2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0},
    {2, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0},

    {2, 1, 2, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 2, 0, 2, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0},
    {2, 0, 0, 0, 2, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0},
    {0, 0, 0, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0},
};

GLuint cursorTexID;
GLuint cursorShaderProgram;
GLuint cursorVAO, cursorVBO, cursorEBO;

float cursorVertices[] = {
    // Positions      // Texture Coords
    0.0f,
    0.0f,
    0.0f,
    0.0f, // Bottom-left
    1.0f,
    0.0f,
    1.0f,
    0.0f, // Bottom-right
    1.0f,
    -1.0f,
    1.0f,
    1.0f, // Top-right
    0.0f,
    -1.0f,
    0.0f,
    1.0f // Top-left
};

// index data
unsigned int cursorIndices[] = {0, 1, 2, 2, 3, 0};

bool initCursorTexture() {
    glGenTextures(1, &cursorTexID);
    glBindTexture(GL_TEXTURE_2D, cursorTexID);

    // convert cursor to RGBA format to cursorTexture
    // 0: transparent, 1: white, 2: black
    GLubyte cursorTexture[16 * 16 * 4];

    for (int y = 0; y < 16; y++) {
        for (int x = 0; x < 16; x++) {
            int index = (y * 16 + x) * 4;
            switch (cursor[y][x]) {
            case 0:
                cursorTexture[index] = 0;
                cursorTexture[index + 1] = 0;
                cursorTexture[index + 2] = 0;
                cursorTexture[index + 3] = 0;
                break;
            case 1:
                cursorTexture[index] = 255;
                cursorTexture[index + 1] = 255;
                cursorTexture[index + 2] = 255;
                cursorTexture[index + 3] = 255;
                break;
            case 2:
                cursorTexture[index] = 0;
                cursorTexture[index + 1] = 0;
                cursorTexture[index + 2] = 0;
                cursorTexture[index + 3] = 255;
                break;
            }
        }
    }

    // Upload the cursor texture
    glTexImage2D(
        GL_TEXTURE_2D,
        0,
        GL_RGBA,
        16,
        16,
        0,
        GL_RGBA,
        GL_UNSIGNED_BYTE,
        cursorTexture
    );

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE);

    const char *vertexShaderSource = R"(
        #version 330 core
        layout(location = 0) in vec2 aPos;       // Vertex position
        layout(location = 1) in vec2 aTexCoord;  // Texture coordinates

        out vec2 TexCoord;  // Texture coordinates to fragment shader

        uniform mat4 projection;
        uniform mat4 model;

        void main() {
            gl_Position = projection * model * vec4(aPos, 0.0, 1.0); // Vertex position
            TexCoord = aTexCoord; // Pass the texture
        }
    )";

    const char *fragmentShaderSource = R"(
        #version 330 core
        out vec4 FragColor;

        in vec2 TexCoord;         // Texture coordinates from vertex shader
        uniform sampler2D uTexture; // Texture sampler

        void main() {
            FragColor = texture(uTexture, TexCoord); // Output the texture
        }
    )";
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, nullptr);
    glCompileShader(vertexShader);

    GLint success;
    glGetShaderiv(vertexShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetShaderInfoLog(vertexShader, 512, nullptr, infoLog);
        printf("ERROR::SHADER::VERTEX::COMPILATION_FAILED\n%s\n", infoLog);
        return false;
    }

    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, nullptr);
    glCompileShader(fragmentShader);

    // Check for shader compile errors
    glGetShaderiv(fragmentShader, GL_COMPILE_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetShaderInfoLog(fragmentShader, 512, nullptr, infoLog);
        printf("ERROR::SHADER::FRAGMENT::COMPILATION_FAILED\n%s\n", infoLog);
        return false;
    }

    cursorShaderProgram = glCreateProgram();
    glAttachShader(cursorShaderProgram, vertexShader);
    glAttachShader(cursorShaderProgram, fragmentShader);
    glLinkProgram(cursorShaderProgram);

    glGetProgramiv(cursorShaderProgram, GL_LINK_STATUS, &success);
    if (!success) {
        char infoLog[512];
        glGetProgramInfoLog(cursorShaderProgram, 512, nullptr, infoLog);
        printf("ERROR::SHADER::PROGRAM::LINKING_FAILED\n%s\n", infoLog);
        return false;
    }

    // remove shaders (no longer needed after linking)
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    glGenVertexArrays(1, &cursorVAO);
    glGenBuffers(1, &cursorVBO);
    glGenBuffers(1, &cursorEBO);

    glBindVertexArray(cursorVAO);

    glBindBuffer(GL_ARRAY_BUFFER, cursorVBO);
    glBufferData(
        GL_ARRAY_BUFFER, sizeof(cursorVertices), cursorVertices, GL_STATIC_DRAW
    );

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, cursorEBO);
    glBufferData(
        GL_ELEMENT_ARRAY_BUFFER,
        sizeof(cursorIndices),
        cursorIndices,
        GL_STATIC_DRAW
    );

    // Position attribute (aPos)
    glVertexAttribPointer(
        0, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void *)0
    );
    glEnableVertexAttribArray(0);

    // Texture attribute (aTexCoord)
    glVertexAttribPointer(
        1, 2, GL_FLOAT, GL_FALSE, 4 * sizeof(float), (void *)(2 * sizeof(float))
    );
    glEnableVertexAttribArray(1);

    glBindVertexArray(0); // Unbind VAO

    return true;
}

// TODO: USE shader
/*
void renderCursor(jint mouseX, jint mouseY) {
    glBindTexture(GL_TEXTURE_2D, cursorTexID);
    glEnable(GL_TEXTURE_2D);
    glBegin(GL_QUADS);
    glTexCoord2f(0.0f, 0.0f);
    glVertex2f(mouseX, mouseY);
    glTexCoord2f(1.0f, 0.0f);
    glVertex2f(mouseX + 16, mouseY);
    glTexCoord2f(1.0f, 1.0f);
    glVertex2f(mouseX + 16, mouseY - 16);
    glTexCoord2f(0.0f, 1.0f);
    glVertex2f(mouseX, mouseY - 16);
    glEnd();
    glDisable(GL_TEXTURE_2D);
}
*/

void renderCursor(jint mouseX, jint mouseY) {
    glUseProgram(cursorShaderProgram);
    glActiveTexture(GL_TEXTURE0);
    glBindTexture(GL_TEXTURE_2D, cursorTexID);
    glUniform1i(glGetUniformLocation(cursorShaderProgram, "uTexture"), 0);
    glm::mat4 model = glm::mat4(1.0f);
    model = glm::translate(model, glm::vec3(mouseX, mouseY, 0.0f));
    model = glm::scale(model, glm::vec3(16.0f, 16.0f, 1.0f));
    glUniformMatrix4fv(
        glGetUniformLocation(cursorShaderProgram, "model"),
        1,
        GL_FALSE,
        glm::value_ptr(model)
    );
    glBindVertexArray(cursorVAO);
    glDrawElements(GL_TRIANGLES, 6, GL_UNSIGNED_INT, 0);
    glBindVertexArray(0);
}

extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_captureFramebufferImpl(
    JNIEnv *env,
    jclass clazz,
    jint textureId,
    jint frameBufferId,
    jint textureWidth,
    jint textureHeight,
    jint targetSizeX,
    jint targetSizeY,
    jint encodingMode,
    jboolean isExtensionAvailable,
    jboolean drawCursor,
    jint xPos,
    jint yPos
) {
    //    glBindTexture(GL_TEXTURE_2D, textureId);
    //    glPixelStorei(GL_PACK_ALIGNMENT, 1); // Set pixel data alignment
    //    auto* pixels = new GLubyte[textureWidth * textureHeight * 3]; // RGB
    //    glGetTexImage(GL_TEXTURE_2D, 0, GL_RGB, GL_UNSIGNED_BYTE, pixels);
    jclass byteStringClass = env->FindClass("com/google/protobuf/ByteString");
    if (byteStringClass == nullptr || env->ExceptionCheck()) {
        // Handle error
        return nullptr;
    }
    jmethodID copyFromMethod = env->GetStaticMethodID(
        byteStringClass, "copyFrom", "([B)Lcom/google/protobuf/ByteString;"
    );
    if (copyFromMethod == nullptr || env->ExceptionCheck()) {
        // Handle error
        return nullptr;
    }
    jbyteArray byteArray = nullptr;
    if (encodingMode == RAW) {
        byteArray = env->NewByteArray(targetSizeX * targetSizeY * 3);
        if (byteArray == nullptr || env->ExceptionCheck()) {
            // Handle error
            return nullptr;
        }
    }
    // **Note**: Flipping should be done in python side.
    glBindFramebuffer(GL_READ_FRAMEBUFFER, frameBufferId);
    auto *pixels = new GLubyte[textureWidth * textureHeight * 3];
    glPixelStorei(GL_PACK_ALIGNMENT, 1);
    glReadPixels(
        0, 0, textureWidth, textureHeight, GL_RGB, GL_UNSIGNED_BYTE, pixels
    );

    // resize if needed
    if (textureWidth != targetSizeX || textureHeight != targetSizeY) {
        auto *resizedPixels = new GLubyte[targetSizeX * targetSizeY * 3];
        for (int y = 0; y < targetSizeY; y++) {
            for (int x = 0; x < targetSizeX; x++) {
                int srcX = x * textureWidth / targetSizeX;
                int srcY = y * textureHeight / targetSizeY;
                int dstIndex = (y * targetSizeX + x) * 3;
                int srcIndex = (srcY * textureWidth + srcX) * 3;
                resizedPixels[dstIndex] = pixels[srcIndex];
                resizedPixels[dstIndex + 1] = pixels[srcIndex + 1];
                resizedPixels[dstIndex + 2] = pixels[srcIndex + 2];
            }
        }
        delete[] pixels;
        pixels = resizedPixels;
    }

    int cursorHeight = 16;
    int cursorWidth = 16;

    // Draw cursor
    if (drawCursor && xPos >= 0 && xPos < targetSizeX && yPos >= 0 &&
        yPos < targetSizeY) {
        for (int dy = 0; dy < cursorHeight; ++dy) {
            for (int dx = 0; dx < cursorWidth; ++dx) {
                int pixelX = xPos + dx;
                int pixelY = yPos + dy;

                // check if the pixel is within the target image
                if (pixelX >= 0 && pixelX < targetSizeX && pixelY >= 0 &&
                    pixelY < targetSizeY) {
                    // Invert y axis
                    int index =
                        ((targetSizeY - pixelY) * targetSizeX + pixelX) *
                        3; // calculate the index of the pixel

                    if (index >= 0 &&
                        index + 2 < textureWidth * textureHeight * 3) {
                        // draw black if color is 2
                        if (cursor[dy][dx] == 2) {
                            pixels[index] = 0;     // Red
                            pixels[index + 1] = 0; // Green
                            pixels[index + 2] = 0; // Blue
                        }
                        // draw white if color is 1
                        else if (cursor[dy][dx] == 1) {
                            pixels[index] = 255;     // Red
                            pixels[index + 1] = 255; // Green
                            pixels[index + 2] = 255; // Blue
                        }
                        // color is 0, do nothing (transparent)
                    }
                }
            }
        }
    }

    // make png bytes from the pixels
    if (encodingMode == PNG) {
#ifdef HAS_PNG
        std::vector<ui8> imageBytes;
        WritePngToMemory(
            (size_t)targetSizeX, (size_t)targetSizeY, pixels, imageBytes
        );
        byteArray = env->NewByteArray(imageBytes.size());
        env->SetByteArrayRegion(
            byteArray,
            0,
            imageBytes.size(),
            reinterpret_cast<jbyte *>(imageBytes.data())
        );
#else
        // Handle error
        env->ThrowNew(
            env->FindClass("java/lang/RuntimeException"),
            "PNG encoding is not supported on this platform: Could not find "
            "libpng"
        );
        return nullptr;
#endif
    } else if (encodingMode == RAW) {
        env->SetByteArrayRegion(
            byteArray,
            0,
            targetSizeX * targetSizeY * 3,
            reinterpret_cast<jbyte *>(pixels)
        );
    }
    jobject byteStringObject =
        env->CallStaticObjectMethod(byteStringClass, copyFromMethod, byteArray);
    if (byteStringObject == nullptr || env->ExceptionCheck()) {
        // Handle error
        if (byteArray != nullptr) {
            env->DeleteLocalRef(byteArray);
        }
        if (pixels != nullptr) {
            delete[] pixels;
        }
        return nullptr;
    }
    // Clean up
    env->DeleteLocalRef(byteArray);
    delete[] pixels;
    return byteStringObject;
}

#ifdef __APPLE__

extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_initializeZerocopyImpl(
    JNIEnv *env,
    jclass clazz,
    jint width,
    jint height,
    jint colorAttachment,
    jint depthAttachment,
    jint python_pid
) {
    if (!initCursorTexture()) {
        fflush(stderr);
        fflush(stdout);
        return nullptr;
    }
    jclass byteStringClass = env->FindClass("com/google/protobuf/ByteString");
    if (byteStringClass == nullptr || env->ExceptionCheck()) {
        return nullptr;
    }
    jmethodID copyFromMethod = env->GetStaticMethodID(
        byteStringClass, "copyFrom", "([B)Lcom/google/protobuf/ByteString;"
    );
    if (copyFromMethod == nullptr || env->ExceptionCheck()) {
        return nullptr;
    }
    void *mach_port = nullptr;
    int size = initializeIoSurface(width, height, &mach_port, python_pid);
    if (size < 0 || mach_port == nullptr) {
        return nullptr;
    }

    jbyteArray byteArray = env->NewByteArray(size);
    if (byteArray == nullptr || env->ExceptionCheck()) {
        // Handle error
        free(mach_port);
        return nullptr;
    }

    env->SetByteArrayRegion(
        byteArray, 0, size, reinterpret_cast<jbyte *>(mach_port)
    );
    jobject byteStringObject =
        env->CallStaticObjectMethod(byteStringClass, copyFromMethod, byteArray);
    if (byteStringObject == nullptr || env->ExceptionCheck()) {
        // Handle error
        if (byteArray != nullptr) {
            env->DeleteLocalRef(byteArray);
        }
        free(mach_port);
        return nullptr;
    }
    env->DeleteLocalRef(byteArray);
    free(mach_port);
    return byteStringObject;
}

extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_captureFramebufferZerocopyImpl(
    JNIEnv *env,
    jclass clazz,
    jint frameBufferId,
    jint targetSizeX,
    jint targetSizeY,
    jboolean drawCursor,
    jint mouseX,
    jint mouseY
) {
    glBindFramebuffer(GL_READ_FRAMEBUFFER, frameBufferId);
    if (drawCursor) {
        renderCursor(mouseX, mouseY);
    }

    // It could have been that the rendered image is already being shared,
    // but the original texture is TEXTURE_2D, so we need to convert to
    // TEXTURE_2D_RECTANGLE_ARB
    copyFramebufferToIOSurface(targetSizeX, targetSizeY);
    return nullptr;
}

#elif defined(HAS_CUDA)
#include "framebuffer_capturer_cuda.h"

extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_initializeZerocopyImpl(
    JNIEnv *env,
    jclass clazz,
    jint width,
    jint height,
    jint colorAttachment,
    jint depthAttachment,
    jint python_pid
) {
    if (!initCursorTexture()) {
        fflush(stderr);
        fflush(stdout);
        return nullptr;
    }
    jclass runtimeExceptionClass = env->FindClass("java/lang/RuntimeException");
    if (runtimeExceptionClass == nullptr) {
        fprintf(stderr, "Failed to find RuntimeException class\n");
        fflush(stderr);
        return nullptr; // JVM automatically throws NoClassDefFoundError
    }

    jclass byteStringClass = env->FindClass("com/google/protobuf/ByteString");
    if (byteStringClass == nullptr || env->ExceptionCheck()) {
        fprintf(stderr, "Failed to find ByteString class\n");
        fflush(stderr);
        return nullptr; // JVM automatically throws NoClassDefFoundError
    }
    jmethodID copyFromMethod = env->GetStaticMethodID(
        byteStringClass, "copyFrom", "([B)Lcom/google/protobuf/ByteString;"
    );
    if (copyFromMethod == nullptr || env->ExceptionCheck()) {
        fprintf(stderr, "Failed to get copyFrom method\n");
        fflush(stderr);
        return nullptr; // JVM automatically throws NoSuchMethodError
    }

    cudaIpcMemHandle_t memHandle;
    int deviceId = -1;
    int size = initialize_cuda_ipc(
        width, height, colorAttachment, depthAttachment, &memHandle, &deviceId
    );

    if (size < 0) {
        fflush(stderr);
        env->ThrowNew(
            runtimeExceptionClass,
            "Failed to initialize CUDA IPC for framebuffer capture"
        );
        return nullptr;
    }

    jbyteArray byteArray = env->NewByteArray(size + sizeof(int));
    if (byteArray == nullptr || env->ExceptionCheck()) {
        // Handle error
        fprintf(stderr, "Failed to create byte array\n");
        fflush(stderr);
        return nullptr;
    }

    env->SetByteArrayRegion(
        byteArray, 0, size, reinterpret_cast<jbyte *>(&memHandle)
    );
    env->SetByteArrayRegion(
        byteArray, size, sizeof(int), reinterpret_cast<jbyte *>(&deviceId)
    );
    jobject byteStringObject =
        env->CallStaticObjectMethod(byteStringClass, copyFromMethod, byteArray);
    if (byteStringObject == nullptr || env->ExceptionCheck()) {
        // Handle error
        fprintf(stderr, "Failed to create ByteString object\n");
        fflush(stderr);
        if (byteArray != nullptr) {
            env->DeleteLocalRef(byteArray);
        }
        return nullptr;
    }
    env->DeleteLocalRef(byteArray);
    return byteStringObject;
}

extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_captureFramebufferZerocopyImpl(
    JNIEnv *env,
    jclass clazz,
    jint frameBufferId,
    jint targetSizeX,
    jint targetSizeY,
    jboolean drawCursor,
    jint mouseX,
    jint mouseY
) {
    glBindFramebuffer(GL_READ_FRAMEBUFFER, frameBufferId);

    if (drawCursor) {
        renderCursor(mouseX, mouseY);
    }

    // CUDA IPC handles are used to share the framebuffer with the Python side
    // However copy is required anyway
    copyFramebufferToCudaSharedMemory(targetSizeX, targetSizeY);
    return nullptr;
}

#else
// Returns an empty ByteString object.
// TODO: Implement this function for normal mmap IPC based one copy. (GPU ->
// CPU)
extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_initializeZerocopyImpl(
    JNIEnv *env,
    jclass clazz,
    jint width,
    jint height,
    jint colorAttachment,
    jint depthAttachment,
    jint python_pid
) {
    jclass byteStringClass = env->FindClass("com/google/protobuf/ByteString");
    if (byteStringClass == nullptr || env->ExceptionCheck()) {
        return nullptr;
    }
    jfieldID emptyField = env->GetStaticFieldID(
        byteStringClass, "EMPTY", "Lcom/google/protobuf/ByteString;"
    );
    if (emptyField == nullptr || env->ExceptionCheck()) {
        return nullptr;
    }
    jobject emptyByteString =
        env->GetStaticObjectField(byteStringClass, emptyField);
    return emptyByteString;
}

// TODO: Implement this function for normal mmap IPC based one copy. (GPU ->
// CPU)
extern "C" JNIEXPORT jobject JNICALL
Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_captureFramebufferZerocopyImpl(
    JNIEnv *env,
    jclass clazz,
    jint frameBufferId,
    jint targetSizeX,
    jint targetSizeY,
    jboolean drawCursor,
    jint mouseX,
    jint mouseY
) {
    return Java_com_kyhsgeekcode_minecraftenv_FramebufferCapturer_captureFramebufferImpl(
        env,
        clazz,
        0,
        frameBufferId,
        targetSizeX,
        targetSizeY,
        targetSizeX,
        targetSizeY,
        RAW,
        false,
        drawCursor,
        mouseX,
        mouseY
    );
}

#endif