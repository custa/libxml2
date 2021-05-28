Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.10
Release: 12
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
Patch0:         libxml2-multilib.patch
# upstream patches
Patch1:   backport-Fix-memory-leak-in-xmlSchemaValidateStream.patch
Patch2:   backport-fix-infinite-loop-in-xmlStringLenDecodeEntities.patch
Patch3:   backport-Updated-python-tests-tstLastError.py.patch
Patch4:   Null-pointer-handling-in-catalog-c.patch 
Patch5:   Fix-overflow-handling-in-xmlBufBackToBuffer.patch
Patch6:   Fix-memory-leak-in-error-path-of-XPath-expr-parser.patch
Patch7:   Fix-memory-leaks-of-encoding-handlers-in-xmlsave-c.patch
Patch8:   Use-random-seed-in-xmlDictComputeFastKey.patch 
Patch9:   Fix-more-memory-leaks-in-error-paths-of-XPath-parser.patch
Patch10:  Fix-freeing-of-nested-documents.patch
Patch11:  Fix-overflow-check-in-xmlNodeDump.patch
Patch12:  Check-for-overflow-when-allocating-two-dimensional-arrays.patch
Patch13:  Fix-integer-overflow-in-xmlBufferResize.patch
Patch14:  Fix-copying-of-entities-in-xmlParseReference.patch
Patch15:  Copy-some-XMLReader-option-flags-to-parser-context.patch
Patch16:  Merge-code-paths-loading-external-entities.patch
Patch17:  Don-t-load-external-entity-from-xmlSAX2GetEntity.patch
Patch18:  Fix-use-after-free-with-validating-reader.patch
Patch19:  Never-expand-parameter-entities-in-text-declaration.patch
Patch20:  Fix-integer-overflow-in-xmlFAParseQuantExact.patch
Patch21:  Report-error-for-invalid-regexp-quantifiers.patch
Patch22:  Add-regexp-regression-tests.patch
Patch23:  Limit-regexp-nesting-depth.patch
Patch24:  Fix-exponential-runtime-in-xmlFARecurseDeterminism.patch
Patch25:  Fix-more-quadratic-runtime-issues-in-HTML-push-parse.patch
Patch26:  Reset-HTML-parser-input-before-reporting-error.patch
Patch27:  Fix-memory-leak-when-shared-libxml-dll-is-unloaded.patch
Patch28:  Fix-memory-leak-in-xmlXIncludeLoadDoc-error-path.patch
Patch29:  Fix-undefined-behavior-in-xmlXPathTryStreamCompile.patch
Patch30:  Fix-integer-overflow-in-htmlParseCharRef.patch
Patch31:  Fix-another-memory-leak-in-xmlSchemaValAtomicType.patch
Patch32:  Fix-integer-overflow-when-parsing-min-max-Occurs.patch
Patch33:  Fix-integer-overflow-in-_xmlSchemaParseGYear.patch
Patch34:  Fix-quadratic-runtime-when-parsing-HTML-script-conte.patch
Patch35:  Fix-UTF-8-decoder-in-HTML-parser.patch
Patch36:  Fix-integer-overflow-when-comparing-schema-dates.patch
Patch37:  Fix-memory-leak-in-xmlXIncludeIncludeNode-error-path.patch
Patch38:  Don-t-recurse-into-xi-include-children-in-xmlXInclud.patch
Patch39:  Don-t-process-siblings-of-root-in-xmlXIncludeProcess.patch
Patch40:  Fix-exponential-runtime-and-memory-in-xi-fallback-pr.patch
Patch41:  Fuzz-XInclude-engine.patch
Patch42:  Fix-memory-leak-in-runtest.c.patch
Patch43:  Fix-XInclude-regression-introduced-with-recent-commi.patch
Patch44:  Fix-memory-leak-in-xmlXIncludeAddNode-error-paths.patch
Patch45:  Fix-double-free-in-XML-reader-with-XIncludes.patch
Patch46:  Limit-size-of-free-lists-in-XML-reader-when-fuzzing.patch
Patch47:  Fix-cleanup-of-attributes-in-XML-reader.patch
Patch48:  Fix-null-deref-in-XPointer-expression-error-path.patch
Patch49:  Fix-use-after-free-when-XIncluding-text-from-Reader.patch

Patch50: backport-Add-test-case-for-recursive-external-parsed-entities.patch
Patch51: backport-Fix-timeout-when-handling-recursive-entities.patch
Patch52: backport-Avoid-call-stack-overflow-with-XML-reader-and-recurs.patch
Patch53: backport-Reset-HTML-parser-input-before-reporting-encoding-er.patch
Patch54: backport-Fix-quadratic-runtime-in-HTML-parser.patch
Patch55: backport-Fix-regression-introduced-with-477c7f6a.patch
Patch56: backport-Fix-HTML-push-parser-lookahead.patch
Patch57: backport-Fix-quadratic-runtime-when-push-parsing-HTML-entity-.patch
Patch58: backport-Fix-quadratic-runtime-in-HTML-push-parser-with-null-.patch
Patch59: backport-Fix-infinite-loop-in-HTML-parser-introduced-with-rec.patch
Patch60: backport-Fix-integer-overflow-in-xmlSchemaGetParticleTotalRan.patch
Patch61: CVE-2021-3517.patch
Patch62: CVE-2021-3518.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python3-devel
BuildRequires: zlib-devel
BuildRequires: pkgconfig
BuildRequires: xz-devel
BuildRequires: libtool
URL: http://xmlsoft.org/

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary: Libraries, includes, etc. to develop XML and HTML applications
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Requires: zlib-devel
Requires: xz-devel
Requires: pkgconfig
Obsoletes: %{name}-static
Provides:  %{name}-static

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select sub nodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package -n python3-%{name}
Summary: Python 3 bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Obsoletes: %{name}-python3 < %{version}-%{release}
Provides: %{name}-python3 = %{version}-%{release}

%description -n python3-%{name}
The libxml2-python3 package contains a Python 3 module that permits
applications written in the Python programming language, version 3, to use the
interface supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%package help
Summary:    Man page for libxml2
BuildArch:  noarch

%description  help
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1

mkdir py3doc
cp doc/*.py py3doc
sed -i 's|#!/usr/bin/python |#!%{__python3} |' py3doc/*.py

%build
./autogen.sh
%configure
%make_build

find doc -type f -exec chmod 0644 \{\} \;

%install
%make_install

make clean
# for python3
%configure --with-python=%{__python3}
%make_install


rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/python*/site-packages/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-%{version}/*
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/libxml2-python-%{version}/*
(cd doc/examples ; make clean ; rm -rf .deps Makefile)
gzip -9 -c doc/libxml2-api.xml > doc/libxml2-api.xml.gz

%check
make runtests

%clean
rm -fr %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS NEWS README Copyright TODO

%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)

%doc AUTHORS NEWS README Copyright
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/tutorial doc/libxml2-api.xml.gz
%doc doc/examples
%doc %dir %{_datadir}/gtk-doc/html/libxml2
%doc %{_datadir}/gtk-doc/html/libxml2/*.devhelp
%doc %{_datadir}/gtk-doc/html/libxml2/*.html
%doc %{_datadir}/gtk-doc/html/libxml2/*.png
%doc %{_datadir}/gtk-doc/html/libxml2/*.css

%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/*
%{_bindir}/xml2-config
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/libxml2/libxml2-config.cmake

%{_libdir}/*a

%files -n python3-%{name}
%defattr(-, root, root)

%{_libdir}/python3*/site-packages/libxml2.py*
%{_libdir}/python3*/site-packages/drv_libxml2.py*
%{_libdir}/python3*/site-packages/__pycache__/*py*
%{_libdir}/python3*/site-packages/libxml2mod*
%doc python/TODO
%doc python/libxml2class.txt
%doc py3doc/*.py
%doc doc/python.html

%files help
%doc %{_mandir}/man1/xml2-config.1*
%doc %{_mandir}/man1/xmllint.1*
%doc %{_mandir}/man1/xmlcatalog.1*
%doc %{_mandir}/man3/libxml.3*


%changelog
* Fri May 28 2021 guoxiaoqi <guoxiaoqi2@huawei.com> - 2.9.10-12
- Type:CVE
- ID:CVE-2021-3537, CVE-2021-3517
- SUG:NA
- DESC:fix CVE-2021-3517 and CVE-2021-3518

* Tue Mar 2 2020 Lirui <lirui130@huawei.com> - 2.9.10-11
- fix problems detected by oss-fuzz test

* Thu Nov 12 2020 Liquor <lirui130@huawei.com> - 2.9.10-10
- fix problems detected by oss-fuzz test

* Thu Oct 29 2020 panxiaohe <panxiaohe@huawei.com> - 2.9.10-9
- remove subpackage python2-libxml2

* Mon Sep 14 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-8
- revert Don-t-try-to-handle-namespaces-when-building-HTML-do.patch.
  rubygem-nokogoro test case fail,because this patch remove xml namespace function.

* Thu Sep 10 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-7
- Fixed some issues found in fuzzing testcases

* Fri Aug 28 2020 zoulin <zoulin13@huawei.com> - 2.9.10-6
- Fix more quadratic runtime issues in HTML push parse
- Fix reset HTML parser input before reporting error

* Wed Aug 12 2020 Liquor <lirui130@huawei.com> - 2.9.10-5
- Limit regexp nesting depth
- Fix exponential runtime in xmlFARecurseDeterminism

* Mon Aug 3 2020 Liquor <lirui130@huawei.com> - 2.9.10-4
- Fix integer overflow in xmlFAParseQuantExact

* Tue Jul 28 2020 shenyangyang <shenyangyang4@huawei.com> - 2.9.10-3
- Fix-use-after-free-with-validating-reader and
  Never-expand-parameter-entities-in-text-declaration

* Fri Jul 3 2020 wangchen <wangchen137@huawei.com> - 2.9.10-2
- Sync some patches from community

* Fri Apr 24 2020 BruceGW <gyl93216@163.com> - 2.9.10-1
- update upstream to 2.9.10

* Tue Mar 17 2020 Leo Fang<leofang_94@163.com> - 2.9.8-9
- Sync some patches from community 

* Thu Dec 19 2019 openEuler Buildteam <buildteam@openEuler.org> - 2.9.8-8
- Delete unused infomation

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-7
- Fix memory leak in xmlSchemaValidateStream

* Fri Sep 20 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-6
- Delete redundant information

* Tue Sep 10 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-5
- Delete epoch

* Thu Sep 5 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.9.8-2
- Backport upstream patches and merge static library to devel package

