var xmlHelpSystemData = "";
xmlHelpSystemData += '<?xml version=\"1.0\" encoding=\"utf-8\"?>';
xmlHelpSystemData += '<WebHelpSystem DefaultUrl=\"content/welcome.html\" Toc=\"Data/Tocs/ToC_for_Help.js\" Index=\"Data/Index.js\" Concepts=\"Data/Concepts.js\" BrowseSequence=\"Data/BrowseSequences/Browse_Sequences__BrowseSequence.js\" Glossary=\"Data/Glossary.js\" SearchDatabase=\"Data/Search.js\" Alias=\"Data/Alias.xml\" Synonyms=\"Data/Synonyms.xml\" SearchFilterSet=\"Data/Filters.js\" PathToScriptsFolder=\"Resources/Scripts/\" SkinName=\"HTML5\" SkinID=\"HTML5\" Multilingual=\"false\" Skins=\"HTML5\" BuildTime=\"9/17/2018 2:57:17 PM\" BuildVersion=\"14.0.6738.27462\" TargetType=\"WebHelp2\" SkinTemplateFolder=\"Skin/\" InPreviewMode=\"false\" TopNavTocPath=\"true\" MoveOutputContentToRoot=\"false\" ReplaceReservedCharacters=\"true\" MakeFileLowerCase=\"true\" UseCustomTopicFileExtension=\"true\" CustomTopicFileExtension=\"html\" PreventExternalUrls=\"false\" EnableResponsiveOutput=\"true\" IncludeGlossarySearchResults=\"true\" ResultsPerPage=\"20\" xml:lang=\"en-us\" LanguageName=\"English\" SearchEngine=\"MadCapSearch\" DebugMode=\"false\">';
xmlHelpSystemData += '    <CatapultSkin Version=\"2\" SkinType=\"WebHelp2\" Comment=\"HTML5 skin\" Anchors=\"Left,Right\" Width=\"1200px\" Height=\"605px\" Top=\"0\" Left=\"0\" Bottom=\"435px\" Right=\"716px\" Tabs=\"TOC,Community\" DefaultTab=\"TOC\" UseBrowserDefaultSize=\"false\" UseDefaultBrowserSetup=\"True\" EnableResponsiveOutput=\"true\" NavigationLinkTop=\"true\" Name=\"HTML5\" SkinID=\"HTML5\" SkinClass=\"_Skins_HTML5\" HideNavOnStartup=\"False\" LogoUrl=\"\">';
xmlHelpSystemData += '        <Toolbar EnableCustomLayout=\"true\" Buttons=\"Print|ExpandAll|Separator|Filler|PreviousTopic|NextTopic\">';
xmlHelpSystemData += '            <Script>$(\'&lt;link&gt;\')';
xmlHelpSystemData += '	.appendTo($(\'head\'))';
xmlHelpSystemData += '	.attr({type: \'text/css\', rel: \'stylesheet\'})';
xmlHelpSystemData += '	.attr(\'href\', \'content/assets/stylesheets/toc_separators.css\');';
xmlHelpSystemData += '';
xmlHelpSystemData += '//Full Screen Images';
xmlHelpSystemData += '$(document).ready(function() {';
xmlHelpSystemData += '  $(\"#topic\").attr({ \"allowfullscreen\": \"\", \"webkitallowfullscreen\": \"\", \"mozallowfullscreen\": \"\"});';
xmlHelpSystemData += '});</Script>';
xmlHelpSystemData += '        </Toolbar>';
xmlHelpSystemData += '    </CatapultSkin>';
xmlHelpSystemData += '</WebHelpSystem>';
MadCap.Utilities.Xhr._FilePathToXmlStringMap.Add('HelpSystem', xmlHelpSystemData);
