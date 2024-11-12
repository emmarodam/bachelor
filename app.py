from bottle import default_app, get, post, run, response, Bottle, request
import git, json

app = Bottle()

# https://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@github.com/emmarodam/bachelor.git

############################## Video setup forbindelse til GitHub
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./bachelor')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""

############################## Skulle komme frem for at teste at Bottle appen virkede
@get("/")
def _():
    return "Jubii"

############################## Token som også står i app.py i vscode

correct_token = "241097"  # Define the correct token

if __name__ == "__main__":
    run(app, host='0.0.0.0', port=8080, debug=True)

##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=80, debug=True, reloader=True)