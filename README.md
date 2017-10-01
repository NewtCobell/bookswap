# bookswap
An open-source project to allow users to more easily share books with their friends and colleagues

I frequently recommend books to my peers that I think they may enjoy.  Often times, I have copies of these books on my e-reader and could easily lend them out, but I don't know when they'll have time to read them (Kindle, for example, lends for two weeks at a time).

I'd like to build a simple acccount-driven portal that allows users to do the following:
1. manage their own profiles
2. list what e-books they have available to lend
3. a link to the amazon (or other) listing to make it easy for other users to find out more about the book
4. a short blurb where the user can (optionally) discuss what they liked about the book
5. an easy way for users to contact one another when they'd like to borrow a book (with a waiting list if it's not available now)

Down the line, I might extend this to physical books, so that my developer community can share technical resources more easily (maybe that Java book that's collecting dust on your bookshelf could help out another local dev who just started a new job that requires Java!).  For self-taught developers and career-switchers, the investment in multiple technical manuals is often steep.  We should share!

This project is built in Python/Django, using Bootstrap for styling.  For now, for the sake of simplicity during early development, I plan to continue using SQLite until it's time to push this out to production, at which point I will likely migrate to PostgreSQL.

Instructions for setting your project's SECRET_KEY can be found in the your_local_settings.py file.  Please rename this file to local_settings.py and set the new key; this way, .gitignore will keep you from pushing the key to GitHub.
