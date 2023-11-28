import argparse
from xml.dom.minidom import parse

parser = argparse.ArgumentParser(description='Extract usefull infos from AndroidManifest.xml')
parser.add_argument('-p','--permissions', help='Show permissions', action='store_true')
parser.add_argument('-a','--activities', help='Show activities', action='store_true')
parser.add_argument('filename')

args = parser.parse_args()

print(args.activities)
dom = parse(args.filename)

if args.permissions is not False:
    permissionsList=[]
    permissions = dom.getElementsByTagName('uses-permission')
    for permission in permissions:
        permissionsList.append(permission.getAttribute('android:name'))

    print("Permissions: ")
    permissionsList.sort()
    for perm in permissionsList:
        print(perm)
    print("")


if args.activities is not False:
    activities = dom.getElementsByTagName('activity')

    mainActivity=""
    activitiesList=[]

    for activity in activities:
        activitiesList.append(activity.getAttribute('android:name'))
        intents = activity.getElementsByTagName('intent-filter')
        for intent in intents:
            actions = intent.getElementsByTagName('action')
            for action in actions:
                if action.getAttribute('android:name') == 'android.intent.action.MAIN':
                    mainActivity = activity.getAttribute('android:name')

    print("MainActivity: ")
    print(mainActivity)
    print(" ")
    print("Activities: ")
    activitiesList.sort()
    for act in activitiesList:
        print(act)
    print("")
