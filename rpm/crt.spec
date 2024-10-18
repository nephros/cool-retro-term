%global qt_version 6.7.2

Name:       cool-retro-term

Summary:    Cool Retro Terminal
Version:    1.2.1
Release:    1
Group:      System/Console
License:    GPLv3+
URL:        https://github.com/Swordfish90/cool-retro-term
Source0:    %{name}-%{version}.tar.xz
Patch0:     SFOS_desktop.patch
Patch1:     SFOS_build.patch
Requires:   qmltermwidget

BuildRequires: pkgconfig(sailfishapp)

BuildRequires: gcc-c++
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtquickcontrols2-devel

%description
cool-retro-term is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.


%prep
%setup -q -n %{name}-%{version}

# SFOS_desktop.patch
%patch0 -p1
# SFOS_build.patch
%patch1 -p1

%build
%{_qmake_qt6}
%make_build

%install
%make_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
