Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.10
Release: 41
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
Patch12:  Check-for-overflow-when-allocating-two-dimensional-a.patch
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

Patch61: backport-CVE-2021-3537.patch
Patch62: CVE-2021-3517.patch
Patch63: CVE-2021-3518.patch
Patch64: Fix-handling-of-unexpected-EOF-in-xmlParseContent.patch
Patch65: Fix-line-numbers-in-error-messages-for-mismatched-ta.patch
Patch66: Fix-null-deref-in-legacy-SAX1-parser.patch
Patch67: update-for-xsd-language-type-check.patch
Patch68: Fix-dangling-pointer-with-xmllint-dropdtd.patch
Patch69: Fix-duplicate-xmlStrEqual-calls-in-htmlParseEndTag.patch
Patch70: Fix-exponential-behavior-with-recursive-entities.patch
Patch71: Fix-quadratic-behavior-when-looking-up-xml-attribute.patch
Patch72: Fix-use-after-free-with-xmllint-html-push.patch
Patch73: Fix-xmlGetNodePath-with-invalid-node-types.patch
Patch74: Stop-checking-attributes-for-UTF-8-validity.patch
Patch75: CVE-2021-3541.patch
Patch76: Fix-corner-case-with-empty-xi-fallback.patch
Patch77: Fix-quadratic-runtime-in-xi-fallback-processing.patch
Patch78: Fix-error-reporting-with-xi-fallback.patch
Patch79: Revert-Fix-quadratic-runtime-in-xi-fallback-processi.patch
Patch80: Remove-dead-code-in-xinclude.c.patch
Patch81: Fix-regression-introduced-with-commit-74dcc10b.patch
Patch82: Fix-regression-introduced-with-commit-d88df4b.patch
Patch83: Make-xmlNodeDumpOutputInternal-non-recursive.patch
Patch84: Fix-NodeDumpOutput-functions.patch
Patch85: Make-htmlNodeDumpFormatOutput-non-recursive.patch
Patch86: Fix-memory-leaks-in-XPointer-string-range-function.patch
Patch87: Fix-null-pointer-deref-in-xmlXPtrRangeInsideFunction.patch
Patch88: Stop-using-maxParserDepth-in-xpath.c.patch
Patch89: Hardcode-maximum-XPath-recursion-depth.patch
Patch90: Fix-XPath-recursion-limit.patch
Patch91: Fix-Null-deref-in-xmlSchemaGetComponentTargetNs.patch
Patch92: Fix-memleaks-in-xmlXIncludeProcessFlags.patch
Patch93: xmlAddChild-and-xmlAddNextSibling-may-not-attach-the.patch
Patch94: Fix-unsigned-integer-overflow-in-htmlParseTryOrFinis.patch
Patch95: Fix-undefined-behavior-in-UTF16LEToUTF8.patch
Patch96: Fix-SEGV-in-xmlSAXParseFileWithData.patch
Patch97: encoding-fix-memleak-in-xmlRegisterCharEncodingHandl.patch
Patch98: Fix-null-deref-in-xmlStringGetNodeList.patch
Patch99: Fix-memory-leak-in-xmlParseElementMixedContentDecl.patch
Patch100:Fix-slow-parsing-of-HTML-with-encoding-errors.patch

Patch101:More-NodeDumpOutput-fixes.patch
Patch102:Don-t-add-formatting-newlines-to-XInclude-nodes.patch
Patch103:Handle-dumps-of-corrupted-documents-more-gracefully.patch
Patch104:Remove-unused-encoding-parameter-of-HTML-output-func.patch
Patch105:Work-around-lxml-API-abuse.patch
Patch106:Fix-regression-in-xmlNodeDumpOutputInternal.patch
Patch107:backport-Revert-Fix-memory-leak-in-xmlParseBalancedChunkMemor.patch
Patch108:backport-xmlParseBalancedChunkMemory-must-not-be-called-with-.patch
Patch109:backport-CVE-2022-23308-Use-after-free-of-ID-and-IDREF-attrib.patch
Patch110:backport-CVE-2022-29824-Fix-integer-overflows-in-xmlBuf-and-xmlBuffer.patch
Patch111:Fix-memory-leaks-for-xmlACatalogAdd.patch
Patch112:Fix-memory-leaks-in-xmlACatalogAdd-when-xmlHashAddEntry-failed.patch
Patch113:backport-CVE-2016-3709.patch
Patch114:backport-pre-CVE-2022-40303-Remove-useless-comparisons.patch
Patch115:backport-CVE-2022-40303-Fix-integer-overflows-with-XML_PARSE_.patch
Patch116:backport-CVE-2022-40304-Fix-dict-corruption-caused-by-entity-.patch
Patch117:backport-schemas-Fix-null-pointer-deref-in-xmlSchemaCheckCOSS.patch
Patch118:backport-parser-Fix-potential-memory-leak-in-xmlParseAttValue.patch
Patch119:backport-CVE-2023-28484-Fix-null-deref-in-xmlSchemaFixupCompl.patch
Patch120:backport-CVE-2023-29469-Hashing-of-empty-dict-strings-isn-t-d.patch
Patch121:backport-Fix-old-SAX1-parser-with-custom-callbacks.patch
Patch122:backport-Always-initialize-SAX1-element-handlers.patch
Patch123:backport-malloc-fail-Fix-memory-leak-in-xmlStaticCopyNodeList.patch
Patch124:backport-CVE-2023-45322.patch
Patch125:backport-CVE-2024-25062.patch
Patch126:backport-CVE-2022-2309.patch
Patch127:backport-CVE-2024-34459.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python2-devel
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
Obsoletes: %{name}-static < %{version}-%{release}
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

%package -n python2-%{name}
%{?python_provide:%python_provide python-%{name}}
Summary: Python bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Provides: %{name}-python = %{version}-%{release}

%description -n python2-%{name}
The libxml2-python package contains a Python 2 module that permits applications
written in the Python programming language, version 2, to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

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

%files -n python2-%{name}
%defattr(-, root, root)

%{_libdir}/python2*/site-packages/libxml2.py*
%{_libdir}/python2*/site-packages/drv_libxml2.py*
%{_libdir}/python2*/site-packages/libxml2mod*
%doc python/TODO
%doc python/libxml2class.txt
%doc python/tests/*.py
%doc doc/*.py
%doc doc/python.html

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
* Tue May 14 2024 cenhuilin <cenhuilin@kylinos.cn> - 2.9.10-41
- Type:CVE
- CVE:CVE-2024-34459
- SUG:NA
- DESC:fix CVE-2024-34459

* Tue Mar 26 zhuofeng <zhuofeng2@huawei.com> - 2.9.10-40
- Type:CVE
- CVE:CVE-2022-2309
- SUG:NA
- DESC:fix CVE-2022-2309

* Mon Feb 19 hehuazhen <hehuazhen@huawei.com> - 2.9.10-39
- Type:CVE
- CVE:CVE-2024-25062
- SUG:NA
- DESC:fix CVE-2024-25062

* Mon Oct 16 hehuazhen <hehuazhen@huawei.com> - 2.9.10-38
- Type:CVE
- CVE:CVE-2023-45322
- SUG:NA
- DESC:fix CVE-2023-45322

* Fri Sep 01 2023 liningjie <liningjie@xfusion.com> - 2.9.10-37
- parser: Fix old SAX1 parser with custom callbacks

* Thu Apr 20 2023 BruceGW <gyl93216@163.com> - 2.9.10-36
- Type:CVE
- CVE:CVE-2023-28484 CVE-2023-29469
- SUG:NA
- DESC:fix CVE-2023-28484CVE-2023-29469

* Mon Nov 21 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-35
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Tue Nov 08 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-34
- fix CVE-2022-40303 CVE-2022-40304

* Wed Sep 14 2022 hubin <hubin73@huawei.com> - 2.9.10-33
- remove recommend in spec

* Tue Sep 13 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-32
- Fix Obsoletes in spec

* Mon Aug 08 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-31
- Type:CVE
- CVE:CVE-2016-3709
- SUG:NA
- DESC:Fix CVE-2016-3709

* Fri Jun 24 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-30
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix memory leaks in xmlACatalogAdd when xmlHashAddEntry failed

* Thu Jun 16 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-29
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:Fix memory leaks for xmlACatalogAdd

* Mon May 09 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-28
- Type:CVE
- ID:CVE-2022-29824
- SUG:NA
- DESC:fix CVE-2022-29824

* Wed Mar 09 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-27
- Type:CVE
- ID:CVE-2022-23308
- SUG:NA
- DESC:fix CVE-2022-23308

* Sat Feb 26 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-26
- fix valgrind errors in xmlParseBalancedChunkMemoryRecover

* Sat Feb 12 2022 fuanan <fuanan3@h-partners.com> - 2.9.10-25
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:use upstream patch refix heap-use-after-free in xmlAddNextSibling and xmlAddChild

* Thu Dec 2 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-24
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:backport upstream patches

* Sat Nov 27 2021 Wentao Fan <fanwentao@huawei.com> - 2.9.10-23
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:revert patches

* Thu Nov 11 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix following issues:
       fix unsigned integer overflow in htmlParseTryOrFinish
       fix undefined behavior in UTF16LEToUTF8
       fix SEGV in xmlSAXParseFileWithData
       encoding: fix memleak in xmlRegisterCharEncodingHandler()
       fix null deref in xmlStringGetNodeList
       fix memory leak in xmlParseElementMixedContentDecl
       fix slow parsing of HTML with encoding errors

* Thu Nov 11 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-21
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix heap-use-after-free in xmlAddNextSibling and xmlAddChild

* Tue Nov 9 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-20
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix memleaks in xmlXIncludeProcessFlags

* Sat Oct 30 2021 huangduirong <huangduirong@huawei.com> - 2.9.10-19
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix fuzz issues, null-deref in xmlSchemaGetComponentTargetNs

* Sat Oct 23 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-18
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix fuzz issues
       fix memory leaks in XPointer string-range function
       fix null pointer deref in xmlXPtrRangeInsideFunction
       stop using maxParserDepth in xpath.c
       hardcode maximum XPath recursion depth
       fix XPath recursion limit

* Thu Oct 21 2021 panxiaohe <panxiaohe@huawei.com> - 2.9.10-17
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:fix fuzz issues
       fix heap-use-after-free in xmlXIncludeIncludeNode
       fix stack overflow in xmlDocDumpMemory
       fix stack overflow in htmlDocContentDumpOutput

* Wed Jun 2 2021 guoxiaoqi <guoxiaoqi2@huawei.com> - 2.9.10-16
- Type:CVE
- ID:CVE-2021-3541
- SUG:NA
- DESC:fix CVE-2021-3541

* Sat May 29 2021 zoulin <zoulin13@huawei.com> - 2.9.10-15
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:[add] patches from upstream
       Fix-handling-of-unexpected-EOF-in-xmlParseContent.patch
       Fix-line-numbers-in-error-messages-for-mismatched-ta.patch
       Fix-null-deref-in-legacy-SAX1-parser.patch
       update-for-xsd-language-type-check.patch
       Fix-dangling-pointer-with-xmllint-dropdtd.patch
       Fix-duplicate-xmlStrEqual-calls-in-htmlParseEndTag.patch
       Fix-exponential-behavior-with-recursive-entities.patch
       Fix-quadratic-behavior-when-looking-up-xml-attribute.patch
       Fix-use-after-free-with-xmllint-html-push.patch
       Fix-xmlGetNodePath-with-invalid-node-types.patch
       Stop-checking-attributes-for-UTF-8-validity.patch

* Fri May 28 2021 guoxiaoqi <guoxiaoqi2@huawei.com> - 2.9.10-14
- Type:CVE
- ID:CVE-2021-3517, CVE-2021-3518
- SUG:NA
- DESC:fix CVE-2021-3517 and CVE-2021-3518

* Wed May 26 2021 yangkang <yangkang90@huawei.com> - 2.9.10-13
- Type:CVE
- ID:CVE-2021-3537
- SUG:NA
- DESC:fix CVE-2021-3537 

* Mon Mar 2 2020 Lirui <lirui130@huawei.com> - 2.9.10-12
- fix problems detected by oss-fuzz test

* Thu Nov 12 2020 Liquor <lirui130@huawei.com> - 2.9.10-11
- fix problems detected by oss-fuzz test

* Thu Nov 12 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-10
- revert Don-t-try-to-handle-namespaces-when-building-HTML-do.patch.
  rubygem-nokogoro test case fail,because this patch remove xml namespace function.

* Thu Nov 12 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-9
- Fixed some issues found in fuzzing testcases

* Fri Nov 6 2020 panxiaohe <panxiaohe@huawei.com> - 2.9.10-8
- add libxml2-help requires

* Thu Oct 15 2020 yangzhuangzhuang <yangzhuangzhuang1@huawei.com> - 2.9.10-7
- Fix CVE-2020-24977

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

