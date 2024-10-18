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
%global qt_version 6.7.2

Name:       qmltermwidget

Summary:    QML Terminal Widget
Version:    0.2.0
Release:    0%{?dist}
Group:      System/X11/Terminals
License:    GPL-2.0+
URL:        https://github.com/Swordfish90/qmltermwidget

Source:    %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(sailfishapp)

BuildRequires: gcc-c++
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{qt_version}
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel

%description
QMLTermWidget is a projekt to enable developers to embed a terminal emulator in QML-based applications.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%{_qmake_qt6}
%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%{_qt6_qmldir}/QMLTermWidget/*
