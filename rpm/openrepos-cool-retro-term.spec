# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       openrepos-cool-retro-term

# >> macros
# << macros

Summary:    Cool Retro Terminal
Version:    1.1.1
Release:    1
Group:      System/Console
License:    GPL-3.0+
URL:        https://github.com/Swordfish90/cool-retro-term
Source0:    %{name}-%{version}.tar.xz
Source100:  openrepos-cool-retro-term.yaml
Requires:   qt5-qtbase
Requires:   qt5-qtbase-gui
Requires:   qt5-qtdeclarative
Requires:   qt5-qtgraphicaleffects
Requires:   qt5-qtquickcontrols
Requires:   libqt5-qtquickcontrols
Requires:   libqt5-qtbase
Requires:   libQt5Gui5
Requires:   libqt5-qtdeclarative
Requires:   libqt5-qtgraphicaleffects
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils

%description
cool-retro-term is a terminal emulator which tries to mimic the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
qmake-qt5
# << build pre


make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# Work around weird qmake behaviour: http://davmac.wordpress.com/2007/02/21/qts-qmake/
make INSTALL_ROOT=%{buildroot} install

desktop-file-install                            \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
%{name}.desktop

# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%doc gpl-2.0.txt gpl-3.0.txt README.md
%{_bindir}/%{name}
%{_libdir}/qt5/qml/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
# >> files
# << files