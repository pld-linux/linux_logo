Summary:	Shows nice ascii logo
Summary(es):	Tux en ASCII (Pingüino del Linux)
Summary(pl):	Program pokazuje ³adne logo Linuksa w ASCII
Summary(pt_BR):	Tux em ASCII (Pingüim do Linux)
Name:		linux_logo
Version:	4.05
Release:	1
License:	GPL
Group:		Applications/Terminal
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
Patch0:		%{name}-pld.patch
Patch1:		%{name}-quote_logo_backslashes.patch
URL:		http://www.glue.umd.edu/~weave/wam/vmwprod/linux_logo/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linux_logo shows a logo in ASCII with some system information.

%description -l pl
linux_logo pokazuje logo Linuksa w ASCII wraz z pewnymi informacjami o
systemie (wersja kernela, rodzaj procesora itp.). ¦wietnie nadaje siê
jako generator ekranów powitalnych przed zalogowaniem siê u¿ytkownika.

%description -l es
Este paquete contiene el tux, pingüino mascota del Linux.

%description -l pt_BR
Este pacote contém o tux, pingüim mascote do Linux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} C_OPTS="%{rpmcflags} -DLINUX_ANSI -I./libsysinfo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install linux_logo $RPM_BUILD_ROOT%{_bindir}
gzip -d linux_logo.1.gz
install	linux_logo.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ANNOUNCE.logo BUGS CHANGES LINUX_LOGO.FAQ README
%doc README.CUSTOM_LOGOS TODO USAGE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
