Summary:	Program that shows nice ascii logo
Summary(es):	Tux en ASCII (Pingüino del Linux)
Summary(pl):	Program pokazuj±cy ³adne logo Linuksa w ASCII
Summary(pt_BR):	Tux em ASCII (Pingüim do Linux)
Name:		linux_logo
Version:	4.09
Release:	3
License:	GPL
Group:		Applications/Terminal
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
# Source0-md5:	ba970437da602e1dbb4c244303793cd6
Patch0:		%{name}-pld.patch
Patch1:		%{name}-quote_logo_backslashes.patch
Patch2:		%{name}-bogus_locale.patch
Patch3:		%{name}-po.patch
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linux_logo shows a logo in ASCII with some system information.

%description -l es
Este paquete contiene el tux, pingüino mascota del Linux.

%description -l pl
linux_logo pokazuje logo Linuksa w ASCII wraz z pewnymi informacjami o
systemie (wersja kernela, rodzaj procesora itp.). ¦wietnie nadaje siê
jako generator ekranów powitalnych przed zalogowaniem siê u¿ytkownika.

%description -l pt_BR
Este pacote contém o tux, pingüim mascote do Linux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{dk,da}.po
mv -f po/{ua,uk}.po

%build
%{__make} \
	CC="%{__cc}" \
	C_OPTS="%{rpmcflags} -DLINUX_ANSI -I./libsysinfo" \
	C_FLAGS="%{rpmcflags} -Wall -I. -I.. -I../include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install linux_logo $RPM_BUILD_ROOT%{_bindir}
gzip -d linux_logo.1.gz
install	linux_logo.1 $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} -C po install \
	INSTALLDIR=$RPM_BUILD_ROOT%{_datadir}/locale

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ANNOUNCE.logo BUGS CHANGES LINUX_LOGO.FAQ README
%doc README.CUSTOM_LOGOS TODO USAGE
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
