%global qt_version 5.15.8

Name:       openrepos-cool-retro-term

# >> macros
# << macros
%define upstream_name cool-retro-term

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

BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-qt5-qtbase-private-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
BuildRequires: opt-qt5-qtdeclarative-devel
BuildRequires: opt-qt5-qtquickcontrols2-devel

Requires: opt-qt5-qtdeclarative%{?_isa} >= %{qt_version}
Requires: opt-qt5-qtgraphicaleffects%{_isa} >= %{qt_version}
Requires: opt-qt5-qtbase-gui >= %{qt_version}

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
# >> setup
# << setup

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%{opt_qmake_qt5}
%make_build

%install
rm -rf %{buildroot}

%make_install

# Work around weird qmake behaviour: http://davmac.wordpress.com/2007/02/21/qts-qmake/
#make INSTALL_ROOT=%%{buildroot} install

# rename files
mv %{buildroot}%{_bindir}/%{upstream_name} %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_datadir}/applications/%{upstream_name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
for f in %{buildroot}%{_datadir}/icons/hicolor/*/apps/%{upstream_name}.png; do
mv ${f}  ${f%/*}/%{name}.png
done

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
