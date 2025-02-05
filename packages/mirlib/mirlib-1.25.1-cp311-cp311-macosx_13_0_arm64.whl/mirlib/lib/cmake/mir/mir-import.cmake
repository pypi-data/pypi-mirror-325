include( CMakeFindDependencyMacro )
find_dependency( eccodes HINTS /tmp/mir/prereqs/eccodeslib/lib/cmake/eccodes )
find_dependency( eckit   HINTS /tmp/mir/prereqs/eckitlib/lib/cmake/eckit )
find_dependency( atlas   HINTS atlas_DIR-NOTFOUND )

set( MIR_LIBRARIES mir )

