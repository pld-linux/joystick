Summary:	Joystick utilities 
Name:		joystick
Version:	1.2.15
Release:	1
License:	GPL
Group:		Utilities
Group(pl):	Narzêdzia
Source0:	ftp://ftp.suse.cz/pub/development/joystick/%{name}-%{version}.tar.gz
URL:		http://www.suse.cz/development/joystick/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes utilities for use with Linux joystick driver:
- jstest
- jscal
- jsattach

%prep
%setup -q

%build
make jstest CFLAGS="$RPM_OPT_FLAGS"
make jscal CFLAGS="$RPM_OPT_FLAGS"
make jsattach CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
strip jstest jscal jsattach
install jstest jscal jsattach $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*
gzip -9nf *.txt || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
