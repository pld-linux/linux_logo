Summary:	Shows nice ascii logo
Summary(pl):	Program pokazuje ³adne logo Linuxa w ASCII
Name:		linux_logo
Version:	3.0b1
Release:	2
Copyright:	GPL
Group:		Utilities
Group(pl):	Narzêdzia
URL:		http://www.glue.umd.edu/~weave/wam/vmwprod/linux_logo
Source:		%{name}-%{version}.tar.gz
Buildroot:	/tmp/%{name}-%{version}-root

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

gzip -9nf linux_logo.1 BUGS CHANGES README TODO USAGE.FAQ

install -s linux_logo $RPM_BUILD_ROOT/usr/bin
install	   linux_logo.1.gz $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS.gz CHANGES.gz README.gz USAGE.FAQ.gz TODO.gz

%attr(755,root,root) /usr/bin/*
/usr/man/man1/*

%changelog
* Sun Mar 14 1999 Micha³ Kuratczyk <kura@pld.org.pl>
  [3.0b1-2]
- sloted BuildRoot into PLD standard
- fixed Group(pl)
- gzipping instead bzipping
- added missing TODO
- removed man group from man page

* Fri Jan 22 1999 Pawe³ Gajda <pagaj@shadow.eu.org>
  [3.0b1-1d]
- first rpm for PLD
