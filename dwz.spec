Summary: DWARF optimization and duplicate removal tool
Name: dwz
Version: 0.12
Release: 1
License: GPLv2+ and GPLv3+
Group: Development/Tools
# git archive --format=tar --remote=git://sourceware.org/git/dwz.git \
#   --prefix=%{name}-%{version}/ %{name}-%{version} \
#   | bzip2 -9 > %{name}-%{version}.tar.xz
Source0: %{name}-%{version}.tar.xz
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

%build
make %{?_smp_mflags} CFLAGS='%{optflags}' LDFLAGS='%{ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir} \
  install

%files
%defattr(-,root,root)
%doc COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%{_mandir}/man1/dwz.1*
