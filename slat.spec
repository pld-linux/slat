Summary:	Tools for information flow analysis of SELinux policies
Summary(pl):	Narzêdzia do analizy przep³ywu informacji dla polityk SELinuksa
Name:		slat
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.nsa.gov/selinux/archives/%{name}-%{version}.tgz
# Source0-md5:	db350dbbe29434c4d3b23ae1ea5c877b
URL:		http://selinux.sf.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

## disable build root strip policy
#%%define __spec_install_post /usr/lib/rpm/brp-compress || :
#%%define debug_package %{nil}
## Binaries created by O'Caml will fail to find the bytecode they
## contain if they are stripped.

%description
Security-Enhanced Linux Analysis Tools (slat) provide a systematic way
to determine if security goals are achieved by a given SELinux policy
configuration. In particular, slat is concerned with information flow
security goals, which describe desired paths by which information
moves throughout a system. We provide a simple syntax in which to
express these goals, and tools that check a policy configuration
against the goals.

%prep
%setup -q

chmod +x configure

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

#%%makeinstall
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*
%{_includedir}/%{name}
%{_infodir}/*.info*
%{_datadir}/%{name}
