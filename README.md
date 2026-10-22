# Hospital Website (Django)

## 1. Run it
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py makemigrations hospital
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Site: http://127.0.0.1:8000/   Admin: http://127.0.0.1:8000/admin/

## 2. Fill in your content (Admin site)
- **Site settings** (create once): hospital name, logo, intro text, About us text, contact details.
- **Services**: add each service (name, description, emoji icon).
- **Gallery images**: upload photos for the home page gallery.
- **Management staff members**: name, role, photo.
- **News posts**, **Job postings**, **Download items**: each appears on its own page.
- **Feedback** / **Contact messages**: tick the entries, choose
  "Download selected as CSV (opens in Excel)" from the Action menu, then click Go.

## 3. Colours
Edit the variables at the top of `static/css/style.css` (--blue, --maroon).

## 4. Before going live
Set a new SECRET_KEY, DEBUG = False and ALLOWED_HOSTS in `config/settings.py`,
and serve the `media/` folder with your web server.
