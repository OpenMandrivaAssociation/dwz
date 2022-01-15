Summary:	DWARF optimization and duplicate removal tool
Name:		dwz
Version:	0.14
Release:	2
License:	GPLv2+ and GPLv3+
Group:		Development/Tools
# git archive --format=tar --remote=git://sourceware.org/git/dwz.git \
#   --prefix=%{name}-%{version}/ %{name}-%{version} \
#   | xz -9 > %{name}-%{version}.tar.xz
Source0:	https://sourceware.org/ftp/dwz/releases/%{name}-%{version}.tar.xz
Patch0:		dwz-0.12-CFLAGS.patch
BuildRequires:	pkgconfig(libelf)
BuildRequires:	pkgconfig(libdw)

%description
The dwz package contains a program that attempts to optimize DWARF
debugging information contained in ELF shared libraries and ELF executables
for size, by replacing DWARF information representation with equivalent
smaller representation where possible and by reducing the amount of
duplication using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information
and using DW_TAG_imported_unit to import it into each CU that needs it.

%prep
%autosetup -p1 -n %{name}

%build
%set_build_flags
%make_build CC=%{__cc} CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}

%files
%doc COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz
%doc %{_mandir}/man1/dwz.1*
