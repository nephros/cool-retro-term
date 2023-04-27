#
# spec file for package QMLTermWidget
#
# Copyright © 2014 Markus S. <kamikazow@web.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
%global qt_version 5.15.8

Name:       qmltermwidget

# filter qml provides
%global __provides_exclude_from ^%{_opt_qt5_archdatadir}/qml/.*\\.so$
%{?opt_qt5_default_filter}

Summary:    QML Terminal Widget
Version:    0.2.0
Release:    0%{?dist}
Group:      System/X11/Terminals
License:    GPL-2.0+
URL:        https://github.com/Swordfish90/qmltermwidget

Source:    %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(sailfishapp)

BuildRequires: opt-qt5-qtbase-devel >= %{qt_version}
BuildRequires: opt-qt5-qtbase-private-devel
%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}
BuildRequires: opt-qt5-qtdeclarative-devel

Requires: opt-qt5-qtdeclarative%{?_isa} >= %{qt_version}
Requires: opt-qt5-qtgraphicaleffects%{_isa} >= %{qt_version}
Requires: opt-qt5-qtbase-gui >= %{qt_version}


%description
QMLTermWidget is a projekt to enable developers to embed a terminal emulator in QML-based applications.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

%{opt_qmake_qt5}
%make_build

%install
# Work around weird qmake behaviour: http://davmac.wordpress.com/2007/02/21/qts-qmake/
#make INSTALL_ROOT=%%{buildroot} install
%make_install

%files
%defattr(-,root,root,-)
%{_opt_qt5_qmldir}/QMLTermWidget/*

%changelog
* Mon Dec 15 21:41:00 UTC 2014 - kamikazow@web.de
- First build
