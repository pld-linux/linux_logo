Summary:	Shows nice ascii logo
Summary(pl):	Program pokazuje ³adne logo Linuxa w ASCII
Name:		linux_logo
Version:	3.9b2
Release:	1
License:	GPL
Group:		Utilities
Group(pl):	Narzêdzia
Source0:	http://www.glue.umd.edu/~weave/wam/vmwprod/linux_logo/%{name}-%{version}.tar.gz
Patch0:		linux_logo-pld.patch
URL:		http://www.glue.umd.edu/~weave/wam/vmwprod/linux_logo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linux_logo shows a logo in ASCII with some system information.

%description -l pl
linux_logo pokazuje logo Linuxa w ASCII wraz z pewnymi informacjami o
systemie (wersja kernela, rodzaj procesora itp.) ¦wietnie nadaje siê jako
generator ekranów powitalnych przed zalogowaniem siê u¿ytkownika.

%prep
%setup -q
%patch0 -p1

%build
# make C_OPTS="$RPM_OPT_FLAGS -DLINUX_ANSI"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

gzip -9nf ANNOUNCE.logo BUGS CHANGES COPYING %{name}-%{version}.lsm \
	LINUX_LOGO.FAQ README README.CUSTOM_LOGOS TODO NEWS linux_logo.1

install -s linux_logo $RPM_BUILD_ROOT%{_bindir}
install	   linux_logo.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.logo.gz BUGS.gz CHANGES.gz COPYING.gz %{name}-%{version}.lsm.gz LINUX_LOGO.FAQ.gz
%doc README.gz README.CUSTOM_LOGOS.gz NEWS.gz TODO.gz
 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
