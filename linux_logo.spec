Summary:	Shows nice ascii logo
Summary(pl):	Program pokazuje ³adne logo Linuxa w ASCII
Name:		linux_logo
Version:	3.0b1
Release:	1d
Copyright:	GPL
Group:		Utilities
Group(pl):	U¿ytki
URL:		http://www.glue.umd.edu/~weave/wam/vmwprod/linux_logo
Source:		%{name}-%{version}.tar.gz
Buildroot:	/tmp/buildroot-%{name}-%{version}

%description
linux_logo shows a logo in ASCII with some system information.

%description -l pl
linux_logo pokazuje logo Linuxa w ASCII wraz z pewnymi informacjami
o systemie (wersja kernela, rodzaj procesora itp.)
¦wietnie nadaje siê jako generator ekranów powitalnych przed zalogowaniem
siê u¿ytkownika.

%prep
%setup -q

%build
make C_OPTS="$RPM_OPT_FLAGS -DLINUX_ANSI"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/man/man1

bzip2 -9 linux_logo.1 BUGS CHANGES README TODO USAGE.FAQ

install -s	linux_logo $RPM_BUILD_ROOT/usr/bin
install		linux_logo.1.bz2 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.bz2 CHANGES.bz2 
%doc README.bz2 USAGE.FAQ.bz2

%attr(644,root, man) /usr/man/man1/*
%attr(755,root,root) /usr/bin/*

%changelog
* Fri Jan 22 1999 Pawe³ Gajda <pagaj@shadow.eu.org>
  [3.0b1-1d]
- first rpm for PLD
