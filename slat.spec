Summary:	Tools for information flow analysis of SELinux policies
Summary(pl.UTF-8):   Narzędzia do analizy przepływu informacji dla polityk SELinuksa
Name:		slat
Version:	1.2.6
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tar.gz
# Source0-md5:	1feb8e69f0d84ca9fe6427894a3bfed0
Patch0:		%{name}-info.patch
URL:		http://selinux.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	ocaml
BuildRequires:	tetex-format-pdflatex
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Binaries created by O'Caml will fail to find the bytecode they
# contain if they are stripped.
%define		_noautostrip		/usr/bin/slat
%define		_enable_debug_packages	0

%description
Security-Enhanced Linux Analysis Tools (slat) provide a systematic way
to determine if security goals are achieved by a given SELinux policy
configuration. In particular, slat is concerned with information flow
security goals, which describe desired paths by which information
moves throughout a system. We provide a simple syntax in which to
express these goals, and tools that check a policy configuration
against the goals.

%description -l pl.UTF-8
Narzędzia slat (Security-Enhanced Linux Analysis Tools) udostępniają
systematyczny sposób na określanie, czy cele bezpieczeństwa zostały
osiągnięte przez daną konfigurację polityki SELinuksa. W szczególności
slat sprawdza cele bezpieczeństwa związane z przepływem informacji,
określające pożądane ścieżki, którymi informacje przenoszą się w
systemie. slat udostępnia prostą składnię określania tych celów oraz
narzędzia sprawdzające zgodność konfiguracji polityki z tymi celami.

%package devel
Summary:	SLAT header files and static libraries
Summary(pl.UTF-8):   Pliki nagłówkowe i biblioteki statyczne SLAT
Group:		Development/Libraries
# doesn't require base

%description devel
SLAT header files and static libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i biblioteki statyczne SLAT.

%prep
%setup -q
%patch0 -p1

chmod +x configure

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/{*.html,*.pdf,disk.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/slatspec.pdf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
%{_infodir}/*.info*

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_includedir}/%{name}
