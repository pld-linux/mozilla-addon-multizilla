Summary:	Advanced panel tool
Summary(pl):	Zaawansowane zarz±dzanie panelami
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
Requires(post,postun):	mozilla
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
Conflicts:	mozilla-addon-tabbrowser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Multizilla is a tool to maintain panels - closing them, opening,
saving their status between sessions. It contains additional toolbar.

%description -l pl
Narzêdzie do zarz±dzania panelami, u³atwiaj±ce zamykanie, otwieranie
paneli oraz zapisywanie ich statusu pomiêdzy sesjami. Zawiera
dodatkowy pasek narzêdziowy.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt ||:
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf} ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome ||:

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf}
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
