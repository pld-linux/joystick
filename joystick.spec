Summary:	Joystick utilities
Summary(pl):	Narz�dzia do obs�ugi joysticka
Name:		joystick
Version:	1.2.15
Release:	2
License:	GPL
Group:		Applications
Source0:	ftp://ftp.suse.cz/pub/development/joystick/%{name}-%{version}.tar.gz
# Source0-md5:	023500eb6986e1a94aa1a0c30af729c2
URL:		http://www.suse.cz/development/joystick/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes utilities for use with Linux joystick driver:
- jstest
- jscal
- jsattach

%description -l pl
Ten pakiet zawiera narz�dzia do u�ywania z linuksowym sterownikiem
joysticka: jstest, jscal, jsattach.

%prep
%setup -q

%build
%{__make} jstest jscal jsattach \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install jstest jscal jsattach $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
