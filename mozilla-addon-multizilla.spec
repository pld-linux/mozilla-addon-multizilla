Summary:	Advanced panel tool
Summary(pl.UTF-8):	Zaawansowane zarządzanie panelami
Name:		mozilla-addon-multizilla
%define		_realname	multiviews
%define	bver	1.6.40
Version:	%{bver}
%define	fver	%(echo %{bver} | tr -d .)
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://mozdev.sweetooth.org/multizilla/%{_realname}-v%{fver}.xpi
# Source0-md5:	eba5652d0b2d0dde86c3eaa575e7ac27
Source1:	%{_realname}-installed-chrome.txt
URL:		http://multizilla.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
Conflicts:	mozilla-addon-tabbrowser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Multizilla is a tool to maintain panels - closing them, opening,
saving their status between sessions. It contains additional toolbar.

%description -l pl.UTF-8
Narzędzie do zarządzania panelami, ułatwiające zamykanie, otwieranie
paneli oraz zapisywanie ich statusu pomiędzy sesjami. Zawiera
dodatkowy pasek narzędziowy.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
