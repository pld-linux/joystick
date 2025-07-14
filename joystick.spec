%define		_snap	20060430
Summary:	Joystick utilities
Summary(pl.UTF-8):	Narzędzia do obsługi joysticka
Name:		joystick
Version:	1.2.15
Patch0:		%{name}-mapping.patch
Release:	2.%{_snap}.2
License:	GPL
Group:		Applications
Source0:	%{name}-%{_snap}.tar.gz
# Source0-md5:	2bb5dee1c20bce9d97bc10c89b830518
URL:		http://linuxconsole.sourceforge.net/input/joystick.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes utilities for use with Linux joystick driver:
- jstest
- jscal
- inputattach
- evtest
- ffset
- fftest

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do używania z linuksowym sterownikiem
joysticka:
- jstest
- jscal
- inputattach
- evtest
- ffset
- fftest

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
%{__make} jstest jscal inputattach evtest ffset fftest\
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install jstest jscal inputattach evtest ffset fftest $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
