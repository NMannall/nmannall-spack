# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *


class RosePicker(PythonPackage):

    """rose_picker - utility for LFRIC."""

    homepage = "https://code.metoffice.gov.uk/svn/lfric/GPL-utilities"

    version("2026.03.2", sha256="9d35cde4edee0069635b8170dd9e017f86f6a8f85b34917fbab545616edd1ce2")
    version("2026.03.1", sha256="a52ef58c088368cf43df0a204c599f974963ee8403bc3357cce402f18cc85fc5")

    depends_on("py-setuptools", type=("build"))

    extends("python@3:")

    def url_for_version(self, version):
        return f"https://github.com/MetOffice/rose_picker/archive/refs/tags/{version}.tar.gz"

    # def install(self, spec, prefix):
    #     install_tree(src=".", dest=prefix, symlinks=True, ignore=None)

    # def setup_run_environment(self, env):
    #     env.prepend_path("PYTHONPATH", self.spec.prefix.lib.python)
