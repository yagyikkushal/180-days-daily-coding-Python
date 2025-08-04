import instaloader

L = instaloader.Instaloader()
username = "yagyikkushal"
# L.load_session_from_file(username)

# Or login if no session is saved
L.login("yagyikkushal", "****")

profile = instaloader.Profile.from_username(L.context, username)

print("Followers:", profile.followers)
print("Posts:", profile.mediacount)
print("Bio:", profile.biography)
print("Following:", profile.followees)