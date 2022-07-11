# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       openrepos-cool-retro-term

# >> macros
# << macros
%define upstream_name cool-retro-term

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Cool Retro Terminal
Version:    1.1.1
Release:    1
Group:      System/Console
License:    GPL-3.0+
URL:        https://github.com/Swordfish90/cool-retro-term
Source0:    %{name}-%{version}.tar.xz
Source100:  openrepos-cool-retro-term.yaml
Patch0:     SFOS_desktop.patch
Patch1:     SFOS_build.patch
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  desktop-file-utils

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
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# Work around weird qmake behaviour: http://davmac.wordpress.com/2007/02/21/qts-qmake/
make INSTALL_ROOT=%{buildroot} install
# rename files
mv %{buildroot}%{_bindir}/%{upstream_name} %{buildroot}%{_bindir}/%{name}
#mv %{buildroot}%{_datadir}/%{upstream_name} %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/applications/%{upstream_name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
for f in %{buildroot}%{_datadir}/icons/hicolor/*/apps/%{upstream_name}.png; do
mv ${f}  ${f%/*}/%{name}.png
done
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}
%{_libdir}/qt5/qml/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
# >> files
# << files
