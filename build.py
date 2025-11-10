import os
import sys
import shutil


GITHUB_WORKSPACE = f"{os.path.abspath(os.curdir)}/build"
OPENSUBDIV_VERSION = "v3_7_0"
OPENUSD_VERSION = "v25.08"
TBB_VERSION = "2021.12.0"
DIST_FOLDER = "openusd-minimal-25.11"

os.makedirs(f"{GITHUB_WORKSPACE}/{DIST_FOLDER}")
os.chdir(GITHUB_WORKSPACE)
os.system(f"wget https://github.com/oneapi-src/oneTBB/releases/download/v{TBB_VERSION}/oneapi-tbb-{TBB_VERSION}-lin.tgz")
os.system(f"tar xzf oneapi-tbb-{TBB_VERSION}-lin.tgz")
shutil.move(f"oneapi-tbb-{TBB_VERSION}/include", f"{GITHUB_WORKSPACE}/{DIST_FOLDER}")
shutil.move(f"oneapi-tbb-{TBB_VERSION}/lib", f"{GITHUB_WORKSPACE}/{DIST_FOLDER}")

os.system(f"git clone --branch {OPENSUBDIV_VERSION} https://github.com/PixarAnimationStudios/OpenSubdiv.git")
os.system(f"cmake -B OpenSubdiv/build -S OpenSubdiv -G Ninja \
    -DCMAKE_INSTALL_PREFIX={GITHUB_WORKSPACE}/{DIST_FOLDER} \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DBUILD_SHARED_LIBS=OFF \
    -DNO_EXAMPLES=1 \
    -DNO_TUTORIALS=1 \
    -DNO_REGRESSION=1 \
    -DNO_PTEX=1 \
    -DNO_DOC=1 \
    -DNO_OMP=1 \
    -DNO_TBB=1 \
    -DNO_CUDA=1 \
    -DNO_OPENCL=1 \
    -DNO_CLEW=1 \
    -DNO_OPENGL=1 \
    -DNO_METAL=1"
)
os.system("cmake --build OpenSubdiv/build --target install")

 
os.system(f"git clone --branch {OPENUSD_VERSION} https://github.com/PixarAnimationStudios/OpenUSD.git")
os.system(f"cmake -B OpenUSD/build -S OpenUSD -G Ninja \
    -DCMAKE_PREFIX_PATH={GITHUB_WORKSPACE}/{DIST_FOLDER} \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DPXR_ENABLE_PYTHON_SUPPORT=OFF \
    -DPXR_ENABLE_GL_SUPPORT=OFF \
    -DPXR_ENABLE_VULKAN_SUPPORT=OFF \
    -DPXR_ENABLE_METAL_SUPPORT=OFF \
    -DPXR_ENABLE_MATERIALX_SUPPORT=OFF \
    -DPXR_ENABLE_OSL_SUPPORT=OFF \
    -DPXR_BUILD_DOCUMENTATION=OFF \
    -DPXR_BUILD_TESTS=OFF \
    -DPXR_BUILD_TUTORIALS=OFF \
    -DPXR_BUILD_EXAMPLES=OFF \
    -DPXR_BUILD_USD_TOOLS=OFF \
    -DPXR_BUILD_IMAGING=OFF \
    -DPXR_BUILD_USD_IMAGING=OFF \
    -DPXR_BUILD_MONOLITHIC=ON \
    -DCMAKE_INSTALL_PREFIX={GITHUB_WORKSPACE}/{DIST_FOLDER}"
)
os.system("cmake --build OpenUSD/build --target install")