# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

from spack_repo.builtin.packages.pfunit.package import Pfunit as BuiltinPfunit


class Pfunit(BuiltinPfunit):

    def setup_run_environment(self, env):
        """Setup custom variables in the generated module file"""
        prefix = self.prefix + "/PFUNIT-" + self.version.up_to(2).string
        env.set("PFUNIT", prefix)
        env.prepend_path("FFLAGS", "-I" + prefix + "/include", " ")
        env.prepend_path("LDFLAGS", "-L" + prefix + "/lib", " ")