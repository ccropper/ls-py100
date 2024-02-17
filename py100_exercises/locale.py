# Write a function that extracts the language code from a locale. A 
# locale is a combination of a language code, a region, and usually 
# also a character set, e.g en_US.UTF-8.

def extract_language(locale):
    locale_split = locale.split('_')
    return locale_split[0]

def extract_region(locale):
    return locale.split('_')[1].split('.')[0]

print(f"For locale en_US.UTF-8, the language code is \
{extract_language('en_US.UTF-8')} and the region is \
{extract_region('en_US.UTF-8')}.")
print(f"For locale en_GB.UTF-8, the language code is \
{extract_language('en_GB.UTF-8')} and the region is \
{extract_region('en_GB.UTF-8')}.")
print(f"For locale ko_KR.UTF-16, the language code is \
{extract_language('ko_KR.UTF-16')} and the region is \
{extract_region('ko_KR.UTF-16')}.")



