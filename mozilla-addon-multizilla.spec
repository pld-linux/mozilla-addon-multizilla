Summary:	Advanced panel tool
Summary(pl):	Zaawansowane zarz±dzanie panelami
Name:		mozilla-addon-multizilla
%define		_realname	multiviews
%define	bver	1.1.20
Version:	%{bver}beta2
%define	fver	%(echo %{bver} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.us-east1.mozdev.org/multizilla/%{_realname}-v%{fver}.xpi
# Source0-md5:	c2da3d764b129196b217c144ed876761
Source1:	%{_realname}-installed-chrome.txt
URL:		http://multizilla.mozdev.org/
BuildRequires:	unzip
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_libdir}/mozilla/chrome

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
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
