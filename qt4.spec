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

%define enable_static 0
%{?_without_static: %{expand: %%global enable_static 0}}

%define with_cups 1
%{?_without_cups %{expand: %%global with_cups 0}}

# Laurent disable for the moment generate pch
%define with_pch 0
%{?_without_pch %{expand: %%global with_pch 0}}

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
%define qtsubminor 0

# KDE development version date
%define kde_copy 1
%define kde_qtcopy_date 20070509

%define qtversion %{qtmajor}.%{qtminor} 
#.%{qtsubminor}

%define qtlib qt4
%define qtdir %_prefix/lib/%{qtlib}
%define pluginsdir %qtdir/plugins/%_lib

%if %{kde_copy}
%define qttarballdir qt-x11-opensource-src-%{qtversion}-%{kde_qtcopy_date}
%else
%define qttarballdir qt-x11-opensource-src-%{qtversion}
%endif

Name: %{qtlib}
Version: %{qtversion}
Release: %mkrel 0.rc1.1
Epoch: 2
Summary: Qt GUI toolkit
Group: Development/KDE and Qt
License: GPL
URL: http://www.trolltech.com/
Source0: ftp://ftp.trolltech.com/qt/source/%{qttarballdir}.tar.bz2
# Not ready yet
#Source1: qt4.sh
#Source2: qt4.csh
Source3: qt4-designer-wrapper
Source4: qt4-designer.desktop
Source5: qt4.macros
Patch0: qt4-uitools-sharedlib.patch
Patch2:	0142-uic3-wordWrapAttribute.diff
Patch4:	qt-x11-opensource-src-4.2.2-pagesize.patch
Patch5:	qt4.3-fix-compile.patch

BuildRequires: glibc-devel

%if %mdkversion <= 200600
BuildRequires: X11-devel
%if %{enable_static}
BuildRequires: X11-static-devel
%endif
%else
BuildRequires: libx11-devel
%if %{enable_static}
BuildRequires: libx11-static-devel
%endif
BuildRequires:  libxrandr-devel
%endif
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
BuildRequires: GL-devel
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

#-------------------------------------------------------------------------

%package -n %{libqdbus}
Summary: QT dbus lib
Summary(pt_BR): Biblioteca do dbus
Group: System/Libraries
Requires(pre): %{name}-common = %epoch:%version
Provides: qdbuslib = %epoch:%version

%description -n %{libqdbus}
QT dbus lib

%post -n %{libqdbus} -p /sbin/ldconfig
%postun -n %{libqdbus} -p /sbin/ldconfig

%files -n %{libqdbus}
%defattr(-,root,root,-)
%{qtdir}/%_lib/libQtDBus.so.*
%{qtdir}/%_lib/libQtDBus.prl

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

#-------------------------------------------------------------------------

%package -n %{libqt}-devel
Summary: Development files and documentation for the Qt GUI toolkit.
Group: Development/KDE and Qt
Requires: %{name}-common = %epoch:%version
Provides: qt4-devel = %epoch:%version-%release
Provides: libqt4-devel = %epoch:%version-%release
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
%{qtdir}/bin/qdbus*
%{qtdir}/bin/pixeltool*
%_sysconfdir/rpm/macros.d/*
%{qtdir}/include
%{qtdir}/mkspecs
%{qtdir}/%_lib/*.so
%{qtdir}/%_lib/*.la
%_libdir/pkgconfig/*
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
Conflicts: %{name}-doc < %{qtversion}-1mdk

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

%description linguist
Qt Linguist provides easy translation of Qt GUIs to different
languages

%post linguist
%update_menus
%if %mdkversion > 200600
%{update_desktop_database}
%endif

%postun linguist
%clean_menus
%if %mdkversion > 200600
%{clean_desktop_database}
%endif

%files linguist
%defattr(-,root,root,-)
%{qtdir}/bin/lingu*
%{qtdir}/bin/lreleas*
%{qtdir}/bin/lupdat*
%_menudir/linguist
%if %mdkversion > 200600
%{_datadir}/applications/*linguist*.desktop
%endif

#-------------------------------------------------------------------------

%package assistant
Summary: QT assistantion doc utility
Group: Books/Computer books
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description assistant
Qt Assistant provides a documentation Browser

%post assistant
%update_menus
%if %mdkversion > 200600
%{update_desktop_database}
%endif

%postun assistant
%clean_menus
%if %mdkversion > 200600
%{clean_desktop_database}
%endif

%files assistant
%defattr(-,root,root,-)
%{qtdir}/bin/assistant*
%_menudir/assistant
%if %mdkversion > 200600
%{_datadir}/applications/*assistant*.desktop
%endif
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
BuildRequires: libmysql-devel

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
%if %mdkversion <= 200600
%_datadir/applnk/Development/designer4.desktop
%endif
%_menudir/%{libqt}-devel-designer
%if %mdkversion > 200600
%{_datadir}/applications/*designer*.desktop
%endif

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
%patch2 -p0 -b .fix_uic3_wordwrap
%patch4 -p1 -b .fix_pagesize
%patch5 -p1 -b .fix_link

%build
export QTDIR=`/bin/pwd`
export PATH=$QTDIR/bin:$PATH
export CFLAGS="${CFLAGS} %{optflags}"
export CXXFLAGS="${CXXFLAGS} %{optflags}"
export YACC='byacc -d'
%if %{kde_copy}
export LD_LIBRARY_PATH=%{_builddir}/qt-copy/lib:$LD_LIBRARY_PATH
export PATH=%{_builddir}/qt-copy/bin:$PATH
%else
export LD_LIBRARY_PATH=%{_builddir}/%{qttarballdir}/lib:$LD_LIBRARY_PATH
export PATH=%{_builddir}/%{qttarballdir}/bin:$PATH
%endif

#--------------------------------------------------------
# function configure
function qt_configure {

echo "yes" |
./configure \
	-prefix %{qtdir} \
        -qdbus \
	-no-pch \
%if %{with_debug}
   -debug-and-release \
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
%if %mdkversion <= 200600   
   -I%_prefix/X11R6/include/ \
   -L%_prefix/X11R6/%_lib \
%endif   
	$*
}

# static
%if %{enable_static}
	qt_configure \
   %if %{with_sqlite}
   -qt-sql-sqlite \
   %endif
   -static

   make sub-src

	mkdir safelib
	cp lib/*.a safelib
%endif

# shared
qt_configure -shared -qdbus \
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
   %else
   -no-sql-sqlite \
   %endif
   %if %{with_odbc}
   -plugin-sql-odbc
   %else
   -no-sql-odbc 
   %endif

make sub-src sub-tools

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

#cp -f %{SOURCE1} %{SOURCE2} %buildroot%_sysconfdir/profile.d

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
cp %{SOURCE3} designer
popd
ln -s %{qtdir}/bin/designer %buildroot%{_bindir}/designer-qt%{qtmajor}

# Desktop
%if %mdkversion <=200600
install -d -m 0755 %buildroot/%_datadir/applnk/Development/
install -m 0644 %SOURCE4 %buildroot/%_datadir/applnk/Development/designer4.desktop
%endif

install -d -m 0755 %buildroot/%_menudir
cat <<EOF > %buildroot/%_menudir/%{libqt}-devel-designer
?package(%{libqt}-devel): needs=X11 \
                        section="More Applications/Development/Development Environments" \
			title="Qt4 Designer" \
			longtitle="A graphical designer/dialog builder for Qt4" \
			command="/usr/bin/designer-qt4" \
			mimetypes="application/x-designer" \
			icon="development_environment_section.png" \
			xdg="true"
EOF

%if %mdkversion > 200600
mkdir $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-designer-qt4.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Qt4 Designer
Comment=A graphical designer/dialog builder for Qt4
Exec=/usr/bin/designer-qt4
Icon=development_environment_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=KDE;QT;Application;X-Mandrivalinux-MoreApplications-Development-DevelopmentEnvironments;
EOF
%endif

cat <<EOF > %buildroot/%_menudir/linguist
?package(qt4-linguist): needs=X11 \
                        section="More Applications/Development/Development Environments" \
			title="Qt Linguist" \
			longtitle="A translation tool for Qt4" \
			command="%qtdir/bin/linguist" \
			mimeType="application/x-linguist" \
			icon="development_environment_section.png" \
			xdg="true"
EOF

%if %mdkversion > 200600
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-linguist-qt4.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Qt Linguist
Comment=A translation tool for Qt4
Exec=%qtdir/bin/linguist
Icon=development_environment_section.png
Terminal=false
Type=Application
StartupNotify=true
MimeType=application/x-linguist
Categories=KDE;QT;Application;X-MandrivaLinux-MoreApplications-Development-DevelopmentEnvironments;
EOF
%endif


#Laurent rename binary program
cat <<EOF > %buildroot/%_menudir/assistant
?package(qt4-assistant): needs=X11 \
			section="More Applications/Documentation" \
			title="Qt4 Assistant" \
			longtitle="A manual browser for Qt4 documentation" \
			command="%{qtdir}/bin/assistant" \
			icon="documentation_section.png" \
			xdg="true"
EOF
%if %mdkversion > 200600
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-assistant-qt4.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Qt4 Assistant
Comment=A manual browser for Qt4 documentation
Exec=%{qtdir}/bin/assistant
Icon=documentation_section.png
Terminal=false
Type=Application
StartupNotify=true
Categories=KDE;QT;Application;X-MandrivaLinux-MoreApplications-Documentation;
EOF
%endif



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

# Move pkgconfig for proper place
mkdir -p %buildroot/%_libdir/pkgconfig
mv %buildroot/%{qtdir}/%_lib/pkgconfig/*.pc %buildroot/%_libdir/pkgconfig


# Fix all buildroot paths
find %buildroot/%qtdir/%_lib -type f -name '*prl' -exec perl -pi -e "s, -L%_builddir/\S+,,g" {} \;
find %buildroot/%qtdir/%_lib -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} \;
find %buildroot/%qtdir/%_lib -type f -name '*la' -print -exec perl -pi -e "s, -L%_builddir/?\S+,,g" {} \;
#find %buildroot/%_libdir/pkgconfig -type f -name '*pc' -print -exec perl -pi -e "s, -L%_builddir/?\S+,,g" {} \;
find %buildroot/%qtdir/mkspecs -name 'qmake.conf' -exec chmod -x -- {} \;
find %buildroot/%qtdir/mkspecs -name Info.plist.app -exec chmod -x -- {} \;

# Install rpm macros
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
install -m 0644 %SOURCE5 %buildroot/%_sysconfdir/rpm/macros.d

%clean
rm -rf %buildroot



