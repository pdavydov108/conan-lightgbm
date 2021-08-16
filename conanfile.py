from conans import ConanFile, CMake, tools


class LightgbmConan(ConanFile):
    name = "lightgbm"
    version = "3.2.1"
    license = "https://github.com/microsoft/LightGBM/blob/master/LICENSE"
    author = "Pavel Davydov pdavydov108@gmail.com"
    url = "https://github.com/microsoft/LightGBM"
    description = "Conan package for lightgbm."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        self.run(f'git clone -b v{self.version} --recursive https://github.com/microsoft/LightGBM')

    def build(self):
        cmake = CMake(self)
        cmake.definitions['BUILD_STATIC_LIB'] = 'ON'
        cmake.configure(source_folder="LightGBM")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["_lightgbm"]

