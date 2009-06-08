Summary:	Program that shows nice ascii logo
Summary(es.UTF-8):	Tux en ASCII (Pingüino del Linux)
Summary(pl.UTF-8):	Program pokazujący ładne logo Linuksa w ASCII
Summary(pt_BR.UTF-8):	Tux em ASCII (Pingüim do Linux)
Name:		linux_logo
Version:	5.05
Release:	1
License:	GPL v2
Group:		Applications/Terminal
Source0:	http://www.deater.net/weave/vmwprod/linux_logo/%{name}-%{version}.tar.gz
# Source0-md5:	f4c5d324774c3a8a42b6f3c9be98bece
Patch0:		%{name}-pld.patch
Patch1:		%{name}-quote_logo_backslashes.patch
Patch2:		%{name}-bogus_locale.patch
Patch3:		%{name}-po.patch
URL:		http://www.deater.net/weave/vmwprod/linux_logo/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
linux_logo shows a logo in ASCII with some system information.

%description -l es.UTF-8
Este paquete contiene el tux, pingüino mascota del Linux.

%description -l pl.UTF-8
linux_logo pokazuje logo Linuksa w ASCII wraz z pewnymi informacjami o
systemie (wersja kernela, rodzaj procesora itp.). Świetnie nadaje się
jako generator ekranów powitalnych przed zalogowaniem się użytkownika.

%description -l pt_BR.UTF-8
Este pacote contém o tux, pingüim mascote do Linux.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{ua,uk}.po

echo 'logos/distributions/pld.logo' > logo_config
find logos -type f -a -not -name 'pld.logo' >> logo_config

%build
./configure \
	--prefix=%{_prefix} dummy-token-to-workaround-configure-bug
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ANNOUNCE.logo BUGS CHANGES* LINUX_LOGO.FAQ README README.CUSTOM_LOGOS TODO USAGE
%attr(755,root,root) %{_bindir}/linux_logo
%{_mandir}/man1/linux_logo.1*
