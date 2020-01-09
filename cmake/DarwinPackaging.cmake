# support creating some basic binpkgs via `make package`

set(CPACK_SET_DESTDIR ON)
set(CPACK_GENERATOR TGZ)

set(CPACK_PACKAGE_VERSION_MAJOR ${LIBSMU_VERSION_MAJOR})
set(CPACK_PACKAGE_VERSION_MINOR ${LIBSMU_VERSION_MINOR})
set(CPACK_PACKAGE_VERSION_PATCH g${LIBSMU_VERSION_PATCH})
set(CPACK_BUNDLE_NAME libsmu)
set(CPACK_PACKAGE_VERSION ${LIBSMU_VERSION_STR})

include(CPack)