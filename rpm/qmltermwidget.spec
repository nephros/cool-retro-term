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

Name:       qmltermwidget
Summary:    QML Terminal Widget
Version:    1.0
Release:    0%{?dist}
Group:      System/X11/Terminals
License:    GPL-2.0+
URL:        https://github.com/Swordfish90/qmltermwidget

Source:    %{name}-%{version}.tar.xz

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: ( pkgconfig(Qt5Declarative) or qt5-qtdeclarative-devel )
BuildRequires: qt5-qtdeclarative-qtquick-devel
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: qt5-qtwidgets-devel

%description
QMLTermWidget is a projekt to enable developers to embed a terminal emulator in QML-based applications.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
qmake-qt5
#make %%{?_smp_mflags}
%make_build

%install
# Work around weird qmake behaviour: http://davmac.wordpress.com/2007/02/21/qts-qmake/
#make INSTALL_ROOT=%%{buildroot} install
%make_install

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/qml/

%changelog
* Mon Dec 15 21:41:00 UTC 2014 - kamikazow@web.de
- First build
