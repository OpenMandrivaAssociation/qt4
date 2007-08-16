%define with_postgres 1
%{?_without_postgres: %{expand: %%global with_postgres 0}}

%define with_mysql 1
%{?_without_mysql: %{expand: %%global with_mysql 0}}

%define with_odbc 1
%{?_without_odbc: %{expand: %%global with_odbc 0}}

%define with_sqlite 1
%{?_without_sqlite: %{expand: %%global with_sqlite 0}}

%define with_ibase 0
%{?_with_ibase: %{expand: %%global with_ibase 1}}

%define with_debug 0
%{?_with_debug: %{expand: %%global with_debug 1}}

%if %{with_debug}
%define dont_strip 1
%endif

%define enable_static 0
%{?_with_static: %{expand: %%global enable_static 1}}

%define with_cups 1
%{?_without_cups %{expand: %%global with_cups 0}}

%define libqt %mklibname qt 4
%define libqassistant %mklibname qassistant 1
%define libqtuitools %mklibname qtuitools 4
%define libqt3support %mklibname qt3support 4
%define libqtcore %mklibname qtcore 4
%define libqtdesigner %mklibname qtdesigner 1
%define libqtgui %mklibname qtgui 4
%define libqtnetwork %mklibname qtnetwork 4
%define libqtopengl %mklibname qtopengl 4
%define libqtsql %mklibname qtsql 4
%define libqtxml %mklibname qtxml 4
%define libqtsvg %mklibname qtsvg 4
%define libqttest %mklibname qttest 4
%define libqdbus %mklibname qtdbus 4
%define libqtscript %mklibname qtscript 4

%define qtmajor 4
%define qtminor 3
%define qtsubminor 1

%define qtversion %{qtmajor}.%{qtminor}.%{qtsubminor} 

%define qtlib qt4
%define qtdir %_prefix/lib/%{qtlib}
%define pluginsdir %qtdir/plugins/%_lib

%define qttarballdir qt-x11-opensource-src-%{qtversion}

Name: %{qtlib}
Version: %{qtversion}
Release: %mkrel 5
Epoch: 2
Summary: Qt GUI toolkit
Group: Development/KDE and Qt
License: GPL
URL: http://www.trolltech.com/
Source0: ftp://ftp.trolltech.com/qt/source/%{qttarballdir}.tar.gz
Source1: qt4-designer-wrapper
Source2: qt4.macros
Source3: mandriva-designer-qt4.desktop 
Source4: mandriva-assistant-qt4.desktop 
Source5: mandriva-linguist-qt4.desktop
Patch0: qt4-uitools-sharedlib.patch
Patch1:	qt4.3-fix-compile.patch
# KDE qt-copy patches
Patch100: 0118-qtcopy-define.diff
Patch101: 0142-uic3-wordWrapAttribute.diff
Patch102: 0172-prefer-xrandr-over-xinerama.diff
Patch103: 0184-dlopen-defaults-to-local.diff
Patch104: 0186-fix-component-alpha-text.diff 
Patch105: 0188-fix-moc-parser-same-name-header.diff
BuildRequires: X11-devel
%if %{enable_static}
BuildRequires: X11-static-devel
%endif
BuildRequires: GL-devel
BuildRequires: Mesa-common-devel
BuildRequires: zlib-devel 
BuildRequires: libpng-devel 
BuildRequires: libjpeg-devel
BuildRequires: libmng-devel
BuildRequires: lcms-devel
BuildRequires: cups-devel
BuildRequires: freetype2-devel
BuildRequires: libfontconfig-devel
BuildRequires: expat-devel
BuildRequires: libdbus-devel >= 0.92
BuildRequires: perl
Provides: %{qtlib}
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt
applications, as well as the README files for Qt.

#------------------------------------------------------------------------

%package common
Group: Development/KDE and Qt
Summary: config, language file for Qt

%description common
This package contains all config file and language file

%files common
%defattr(-,root,root,-)
%{_bindir}/qt4config
%{qtdir}/bin/qtconfig*
%_sysconfdir/ld.so.conf.d/*
%attr(0755,root,root) %_sysconfdir/profile.d/*
%dir %{qtdir}
%dir %{qtdir}/bin
%dir %{qtdir}/%_lib
%dir %pluginsdir
%dir %pluginsdir/sqldrivers
%{qtdir}/phrasebooks
%_docdir/%name/README

#------------------------------------------------------------------------
# CORE QT LIBRARIES
#-------------------------------------------------------------------------

%package -n %{libqtxml}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides:	qtxmllib = %epoch:%version

%description -n %{libqtxml}
QT%{qtmajor} component library

%post -n %{libqtxml} -p /sbin/ldconfig
%postun -n %{libqtxml} -p /sbin/ldconfig

%files -n %{libqtxml}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtXml.so.*
%{qtdir}/%_lib/libQtXml.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtsql}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides:	qtsqllib = %epoch:%version 

%description -n %{libqtsql}
QT%{qtmajor} component library

%post -n %{libqtsql} -p /sbin/ldconfig
%postun -n %{libqtsql} -p /sbin/ldconfig

%files -n %{libqtsql}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtSql.so.*
%{qtdir}/%_lib/libQtSql.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtnetwork}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtnetworklib = %epoch:%version

%description -n %{libqtnetwork}
QT%{qtmajor} component library

%post -n %{libqtnetwork} -p /sbin/ldconfig
%postun -n %{libqtnetwork} -p /sbin/ldconfig

%files -n %{libqtnetwork}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtNetwork.so.*
%{qtdir}/%_lib/libQtNetwork.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtscript}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: libqtscript = %epoch:%version

%description -n %{libqtscript}
QT%{qtmajor} component library

%post -n %{libqtscript} -p /sbin/ldconfig
%postun -n %{libqtscript} -p /sbin/ldconfig

%files -n %{libqtscript}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtScript.so.*
%{qtdir}/%_lib/libQtScript.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtgui}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Conflicts: %{libqtcore} <= 2:4.2.2-%mkrel 2
Provides: qtguilib = %epoch:%version

%description -n %{libqtgui}
QT%{qtmajor} component library

%post -n %{libqtgui} -p /sbin/ldconfig
%postun -n %{libqtgui} -p /sbin/ldconfig

%files -n %{libqtgui}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtGui.so.*
%{qtdir}/%_lib/libQtGui.prl
%pluginsdir/imageformats
%pluginsdir/inputmethods/libqimsw-multi.so*
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtsvg}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtsvglib = %epoch:%version

%description -n %{libqtsvg}
QT%{qtmajor} component library

%post -n %{libqtsvg} -p /sbin/ldconfig
%postun -n %{libqtsvg} -p /sbin/ldconfig

%files -n %{libqtsvg}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtSvg.so.*
%{qtdir}/%_lib/libQtSvg.prl
%pluginsdir/iconengines/libqsvg.so*
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqttest}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qttestlib = %epoch:%version

%description -n %{libqttest}
QT%{qtmajor} component library

%post -n %{libqttest} -p /sbin/ldconfig
%postun -n %{libqttest} -p /sbin/ldconfig

%files -n %{libqttest}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtTest.so.*
%{qtdir}/%_lib/libQtTest.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtcore}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Conflicts: %{libqtgui} <= 2:4.2.2-%mkrel 2
Provides: qtcorelib = %epoch:%version

%description -n %{libqtcore}
QT%{qtmajor} component library

%post -n %{libqtcore} -p /sbin/ldconfig
%postun -n %{libqtcore} -p /sbin/ldconfig

%files -n %{libqtcore}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtCore.so.*
%{qtdir}/%_lib/libQtCore.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqt3support}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qt3supportlib = %epoch:%version

%description -n %{libqt3support}
QT%{qtmajor} component library

%post -n %{libqt3support} -p /sbin/ldconfig
%postun -n %{libqt3support} -p /sbin/ldconfig

%files -n %{libqt3support}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQt3Support.so.*
%{qtdir}/%_lib/libQt3Support.prl
%pluginsdir/designer/libqt3supportwidgets.so*
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtopengl}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtopengllib = %epoch:%version

%description -n %{libqtopengl}
QT%{qtmajor} component library

%post -n %{libqtopengl} -p /sbin/ldconfig
%postun -n %{libqtopengl} -p /sbin/ldconfig

%files -n %{libqtopengl}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtOpenGL.so.*
%{qtdir}/%_lib/libQtOpenGL.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtdesigner}
Summary: QT%{qtmajor} component library
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtdesignerlib = %epoch:%version

%description -n %{libqtdesigner}
QT%{qtmajor} component library

%description -l pt_BR -n %{libqtdesigner}
Biblioteca componente da QT%{qtmajor}

%post -n %{libqtdesigner} -p /sbin/ldconfig
%postun -n %{libqtdesigner} -p /sbin/ldconfig

%files -n %{libqtdesigner}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtDesigner.so.*
%{qtdir}/%_lib/libQtDesigner.prl
%{qtdir}/%_lib/libQtDesignerComponents.so.*
%{qtdir}/%_lib/libQtDesignerComponents.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqtuitools}
Summary: QT assistant lib
Summary(pt_BR): Biblioteca do qt-assistant
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qtuitoolslib = %epoch:%version

%description -n %{libqtuitools}
QT assistant lib

%post -n %{libqtuitools} -p /sbin/ldconfig
%postun -n %{libqtuitools} -p /sbin/ldconfig

%files -n %{libqtuitools}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtUiTools.so.*
%{qtdir}/%_lib/libQtUiTools.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqdbus}
Summary: QT dbus lib
Summary(pt_BR): Biblioteca do dbus
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qdbuslib = %epoch:%version
Conflicts: qt4-devel < 2:4.3.0 

%description -n %{libqdbus}
QT dbus lib

%post -n %{libqdbus} -p /sbin/ldconfig
%postun -n %{libqdbus} -p /sbin/ldconfig

%files -n %{libqdbus}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtDBus.so.*
%{qtdir}/%_lib/libQtDBus.prl
%{qtdir}/bin/qdbus*
%if ! %{with_debug}
%exclude %{qtdir}/bin/qdbus*.debug
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqassistant}
Summary: QT assistant lib
Summary(pt_BR): Biblioteca do qt-assistant
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qassistantlib = %epoch:%version

%description -n %{libqassistant}
QT assistant lib

%post -n %{libqassistant} -p /sbin/ldconfig
%postun -n %{libqassistant} -p /sbin/ldconfig

%files -n %{libqassistant}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtAssistantClient.so.*
%{qtdir}/%_lib/libQtAssistantClient.prl
%if ! %{with_debug}
%exclude %{qtdir}/%_lib/lib*.debug
%endif

#-------------------------------------------------------------------------

%package -n %{libqt}-devel
Summary: Development files for the Qt GUI toolkit.
Group: Development/KDE and Qt
Requires: %{name}-common = %epoch:%version
Provides: qt4-devel = %epoch:%version-%release
Provides: libqt4-devel = %epoch:%version-%release
Conflicts: %{libqdbus} < 2:4.3.0 
# There's symlinks to devel
Requires: %{libqassistant} = %epoch:%version-%release
Requires: %{libqtuitools} = %epoch:%version-%release
Requires: %{libqt3support} = %epoch:%version-%release
Requires: %{libqtcore} = %epoch:%version-%release
Requires: %{libqtdesigner} = %epoch:%version-%release
Requires: %{libqtgui} = %epoch:%version-%release
Requires: %{libqtnetwork} = %epoch:%version-%release
Requires: %{libqtopengl} = %epoch:%version-%release
Requires: %{libqtsql} = %epoch:%version-%release
Requires: %{libqtxml} = %epoch:%version-%release
Requires: %{libqtsvg} = %epoch:%version-%release
Requires: %{libqttest} = %epoch:%version-%release
Requires: %{libqdbus} = %epoch:%version-%release

%description -n %{libqt}-devel
The %{qtlib}-devel package contains the files necessary to develop
applications using the Qt GUI toolkit: the header files, the Qt
meta object compiler, and the static libraries.  See the address
http://www.trolltech.com/products/qt.html for more information
about Qt.
Install qt-devel if you want to develop GUI applications using the Qt
toolkit.

%files -n %{libqt}-devel
%defattr(-,root,root,-)
%{qtdir}/bin/moc*
%{qtdir}/bin/qmake*
%{qtdir}/bin/uic*
%{qtdir}/bin/rcc*
%{qtdir}/bin/qt3to4*
%{qtdir}/bin/pixeltool*
%_sysconfdir/rpm/macros.d/*
%{qtdir}/include
%{qtdir}/mkspecs
%{qtdir}/%_lib/*.so
%{qtdir}/%_lib/*.la
%{qtdir}/%_lib/pkgconfig/*
%{qtdir}/q3porting.xml

#-------------------------------------------------------------------------

%if %{enable_static}
%package -n %{libqt}-static-devel
Summary: The static library for the Qt GUI toolkit
Group:		Development/KDE and Qt 

%description -n %{libqt}-static-devel
Qt is a GUI software toolkit which simplifies the task of writing and
maintaining GUI (Graphical User Interface) applications for the X
Window System. Qt is written in C++ and is fully object-oriented.

This package contains the shared library needed to run Qt
applications, as well as the README files for Qt.

%files -n %{libqt}-static-devel
%defattr(-,root,root,-)
%{qtdir}/%_lib/*.a

%endif

#-------------------------------------------------------------------------

%package doc
Summary: HTML Documentation for Qt version %{version}
Group: Books/Computer books

%description doc
HTML documentation for the Qt toolkit. To view the documentation,
please load up the file /usr/lib/%{qtlib}/doc/html/index.html in your
favourite browser.

%post doc
# Remove old qt4 doc directories
find %_docdir -maxdepth 1 -type d -name qt-4.\* -exec rm -rf {} \;

%files doc
%defattr(-,root,root,-)
%_docdir/%name/doc/html

#-------------------------------------------------------------------------

%package examples
Summary: Example programs made with Qt version %{version}
Group: Books/Computer books

%description examples
Example programs made with Qt version %{version}.

%files examples
%defattr(-,root,root,-)
%{_docdir}/%name/examples
%{_docdir}/%name/demos
%exclude %{_docdir}/%name/examples/tutorial

#-------------------------------------------------------------------------

%package linguist
Summary: QT linguist translation utility
Group: Books/Computer books
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts: qt3-linguist

%description linguist
Qt Linguist provides easy translation of Qt GUIs to different
languages

%post linguist
%update_menus
%{update_desktop_database}

%postun linguist
%clean_menus
%{clean_desktop_database}

%files linguist
%defattr(-,root,root,-)
%{qtdir}/bin/lingu*
%{qtdir}/bin/lreleas*
%{qtdir}/bin/lupdat*
%{_datadir}/applications/*linguist*.desktop

#-------------------------------------------------------------------------

%package assistant
Summary: QT assistantion doc utility
Group: Books/Computer books
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
Conflicts: qt3-assistant

%description assistant
Qt Assistant provides a documentation Browser

%post assistant
%update_menus
%{update_desktop_database}

%postun assistant
%clean_menus
%{clean_desktop_database}

%files assistant
%defattr(-,root,root,-)
%{qtdir}/bin/assistant*
%{_datadir}/applications/*assistant*.desktop

#-------------------------------------------------------------------------

%package tutorial
Summary: Tutorial programs for Qt version %{version}
Group: Books/Computer books

%description tutorial
Tutorial programs for Qt version %{version}.

%files tutorial
%defattr(-,root,root,-)
%{_docdir}/%name/examples/tutorial

#-------------------------------------------------------------------------

%if %{with_odbc}

%package database-plugin-odbc-%_lib
Summary: Database plugin for ODBC Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-odbc
BuildRequires: unixODBC-devel
%if %{enable_static}
BuildRequires: unixODBC-static-devel
%endif

%description database-plugin-odbc-%_lib
Database plugin for ODBC Qt support

%files database-plugin-odbc-%_lib
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlodbc*

%endif

#-------------------------------------------------------------------------

%if %{with_mysql}

%package database-plugin-mysql-%_lib
Summary: Database plugin for mysql Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-mysql
BuildRequires: mysql-devel

%description database-plugin-mysql-%_lib
Database plugin for mysql Qt support

%files database-plugin-mysql-%_lib
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlmysql*

%endif

#-------------------------------------------------------------------------

%if %{with_sqlite}

%package database-plugin-sqlite-%_lib
Summary: Database plugin for sqlite Qt support
Group: Databases
Obsoletes: qt4-database-plugin-sqlite
BuildRequires: sqlite3-devel
%if %{enable_static}
BuildRequires: sqlite3-static-devel
%endif

%description database-plugin-sqlite-%_lib
Database plugin for sqlite Qt support

%files database-plugin-sqlite-%_lib
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlite*
%endif

#-------------------------------------------------------------------------

%if %{with_ibase}

%package database-plugin-ibase-%_lib
Summary: Database plugin for interbase Qt support
Group: Development/KDE and Qt
Obsoletes: qt4-database-plugin-ibase
BuildRequires: firebird-devel

%description database-plugin-ibase-%_lib
Database plugin for interbase Qt support

%files database-plugin-ibase-%_lib
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlibase*
%endif

#-------------------------------------------------------------------------

%if %{with_postgres}

%package database-plugin-pgsql-%_lib
Summary: Database plugin for pgsql Qt support
Group: Development/KDE and Qt
Obsoletes: %name-database-plugin-pgsql
BuildRequires: postgresql-devel

%description database-plugin-pgsql-%_lib
Database plugin for pgsql Qt support

%files database-plugin-pgsql-%_lib
%defattr(-,root,root,-)
%pluginsdir/sqldrivers/libqsqlpsql*

%endif

#-------------------------------------------------------------------------

%package accessibility-plugin-%_lib
Summary: Accessibility plugins for Qt4
Group: Development/KDE and Qt
Obsoletes: %name-accessibility-plugin
Obsoletes: %name-accessibility-plugins

%description accessibility-plugin-%_lib
Acessibility plugins for Qt4

%files accessibility-plugin-%_lib
%defattr(-,root,root,-)
%dir %pluginsdir/accessible
%pluginsdir/accessible/*

#-------------------------------------------------------------------------

%package codecs-plugin-%_lib
Summary: codecs plugins for Qt4
Group: 	Development/KDE and Qt
Obsoletes: %name-codecs-plugin
Obsoletes: %name-codecs-plugins

%description codecs-plugin-%_lib
Acessibility plugins for Qt4

%files codecs-plugin-%_lib
%defattr(-,root,root,-)
%dir %pluginsdir/codecs
%pluginsdir/codecs/*.so*

#-------------------------------------------------------------------------

%package designer
Summary: %{qtlib} visual design tool
Group: Development/KDE and Qt
Requires: %{libqt}-devel = %epoch:%version

%description designer
The Qt Designer is a visual design tool that makes designing and
implementing user interfaces a lot easier.

%post designer
%update_menus

%postun designer
%clean_menus


%files designer
%defattr(-,root,root,-)
%{_bindir}/designer-qt%{qtmajor}
%{qtdir}/bin/designer*
%{_datadir}/applications/*designer*.desktop
%exclude %{qtdir}/bin/*.debug

#-------------------------------------------------------------------------

%package qvfb
Summary: %{qtlib} embedded virtual terminal
Group: Development/KDE and Qt

%description qvfb
Qt 4 Embedded Virtual Terminal

%files qvfb
%defattr(-,root,root,-)
%{qtdir}/bin/qvf*

#-------------------------------------------------------------------------

%prep
%setup -q -n %{qttarballdir}
%patch0 -p1 -b .uilib
%patch1 -p1 -b .fix_link
# qt-copy patches
%patch100 -p0 -b .qt-copy
%patch101 -p0 -b .qt-copy
%patch102 -p0 -b .qt-copy
%patch103 -p0 -b .qt-copy
%patch104 -p0 -b .qt-copy
%patch105 -p0 -b .qt-copy

%build
export QTDIR=`/bin/pwd`
export PATH=$QTDIR/bin:$PATH
export CPPFLAGS="${CFLAGS} %{optflags} -fPIC"
export CXXFLAGS="${CXXFLAGS} %{optflags} -fPIC"
export YACC='byacc -d'
export LD_LIBRARY_PATH=%{_builddir}/%{qttarballdir}/lib:$LD_LIBRARY_PATH
export PATH=%{_builddir}/%{qttarballdir}/bin:$PATH

#--------------------------------------------------------
# function configure
function qt_configure {

echo "yes" |
./configure \
	-prefix %{qtdir} \
	-qdbus \
%if %{with_debug}
   -debug \
%else
   -release \
%endif
   -sysconfdir %_sysconfdir \
   -libdir %{qtdir}/%_lib \
   -docdir %_docdir/%name/doc \
   -plugindir %pluginsdir \
   -qvfb \
   -qt-gif \
%if ! %{with_cups}
   -no-cups \
%endif
   -no-exceptions \
   -L%_prefix/%_lib \
   -platform linux-g++ \
   -confirm-license \
   -verbose \
	$*
}

# static
%if %{enable_static}
	qt_configure \
   %if %{with_odbc}
   -qt-sql-odbc \
   %endif
   %if %{with_sqlite}
   -qt-sql-sqlite \
   -no-sql-sqlite2 \
   %else
   -no-sql-sqlite \
   -no-sql-sqlite2 \
   %endif
   -nomake demos \
   -nomake examples \
   -nomake tools \
   -static

   %make

	mkdir safelib
	cp lib/*.a safelib
%endif

# shared
qt_configure -shared \
   %if %{with_postgres}
   -plugin-sql-psql \
        -no-pch \
   -I%{_includedir}/pgsql \
   -I%{_includedir}/pgsql/server \
   %endif
   %if %{with_mysql}
   -plugin-sql-mysql \
   -I%{_includedir}/mysql \
   %else
   -no-sql-mysql \
   %endif
   %if %{with_ibase}
   -plugin-sql-ibase \
   %else
   -no-sql-ibase \
   %endif
   %if %{with_sqlite}
   -plugin-sql-sqlite \
   -no-sql-sqlite2 \
   %else
   -no-sql-sqlite \
   -no-sql-sqlite2 \
   %endif
   %if %{with_odbc}
   -plugin-sql-odbc \
   %else
   -no-sql-odbc \
   %endif
   -nomake demos \
   -nomake examples 

%make 

# Compile qvfb
pushd tools/qvfb
   make 
popd

%install
rm -rf %buildroot
install -d %buildroot%_bindir
install -d %buildroot%_docdir/%name
install -d %buildroot%_sysconfdir
install -d %buildroot%_sysconfdir/profile.d
install -d %buildroot%_sysconfdir/ld.so.conf.d

make INSTALL_ROOT=%buildroot \
	sub-tools-install_subtargets-ordered \
	install_htmldocs \
	install_qmake \
	install_mkspecs

install -m 0644 README %buildroot%_docdir/%name

# Install qvfb
pushd tools/qvfb
   make INSTALL_ROOT=%buildroot install
popd

# Designer wrapper
pushd  %buildroot%{qtdir}/bin
mv designer designer-real
cp %SOURCE1 designer
popd
ln -s %{qtdir}/bin/designer %buildroot%{_bindir}/designer-qt%{qtmajor}

mkdir -p %buildroot%_datadir/applications
install -m 644 %SOURCE3 %buildroot%_datadir/applications
install -m 644 %SOURCE4 %buildroot%_datadir/applications
install -m 644 %SOURCE5 %buildroot%_datadir/applications

# qtconfig
ln -s %{qtdir}/bin/qtconfig %buildroot%{_bindir}/qt4config

# Fix mkspec link
pushd  %buildroot%{qtdir}/mkspecs
rm -f default
ln -sf %{qtdir}/mkspecs/linux-g++ default
popd

# Copy examples/tutorial and demos
for subdir in examples demos; do
   for dir in `find $subdir -type d -name .obj`; do rm -rf $dir; done
   for dir in `find $subdir -type d -name .moc`; do rm -rf $dir; done
   cp -a $subdir %buildroot/%_docdir/%name
done

%if %{enable_static}
	cp safelib/* %buildroot/%{qtdir}/%_lib
%endif

# Use the new ld.so.conf.d 
pushd %buildroot/%_sysconfdir/ld.so.conf.d
echo "%{qtdir}/%_lib" > qt4.conf
popd

# Fix all buildroot paths
find %buildroot/%qtdir/%_lib -type f -name '*prl' -exec perl -pi -e "s, -L%_builddir/\S+,,g" {} \;
find %buildroot/%qtdir/%_lib -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} \;
find %buildroot/%qtdir/%_lib -type f -name '*la' -print -exec perl -pi -e "s, -L%_builddir/?\S+,,g" {} \;
find %buildroot/%qtdir/mkspecs -name 'qmake.conf' -exec chmod -x -- {} \;
find %buildroot/%qtdir/mkspecs -name Info.plist.app -exec chmod -x -- {} \;

# Install rpm macros
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
install -m 0644 %SOURCE2 %buildroot/%_sysconfdir/rpm/macros.d

# Profiles
cat > %buildroot%_sysconfdir/profile.d/qt4.sh << EOF
#!/bin/bash

if [ -z \$PKG_CONFIG_PATH ]; then
    PKG_CONFIG_PATH=%{qtdir}/%_lib/pkgconfig
else
    PKG_CONFIG_PATH=\${PKG_CONFIG_PATH}:%{qtdir}/%_lib/pkgconfig
fi

function qt4env {
    QTDIR=%{qtdir}
    PATH=%{qtdir}/bin:\${PATH}

    export QTDIR PATH
}

export PKG_CONFIG_PATH
EOF

%clean
rm -rf %buildroot



