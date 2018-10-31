Summary: DWARF optimization and duplicate removal tool
Name: dwz
Version: 0.12
Release: 4
License: GPLv2+ and GPLv3+
Group: Development/Tools
# git archive --format=tar --remote=git://sourceware.org/git/dwz.git \
#   --prefix=%{name}-%{version}/ %{name}-%{version} \
#   | bzip2 -9 > %{name}-%{version}.tar.xz
Source0: %{name}-%{version}.tar.xz
Patch0: dwz-0.12-CFLAGS.patch
# From upstream
# https://sourceware.org/git/?p=dwz.git;a=commitdiff;h=2124f9b50c2c4963e1ac6f1716ca48b114643ca8;hp=be35c03955bcf6e4e4a1cab1af46bb4e729284b3
# see also https://bugzilla.redhat.com/show_bug.cgi?id=1507468
# occurs e.g. when building gdb 8.1 on armv7hl
Patch1: dwz-DW_OP_GNU_variable_value.patch
BuildRequires: pkgconfig(libelf)
BuildRequires: pkgconfig(libdw)

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%setup -q
%autopatch -p1

%build
%make_build CC=%{__cc} CFLAGS='%{optflags}' LDFLAGS='%{ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%files
%doc COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz.1*
