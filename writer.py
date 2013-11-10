import json
import os

PATHSEP="\\"
if os.name=="posix":
	PATHSEP="/"

def filename(team, run):
	return team+PATHSEP+str(run)+".run"

def readRun(team,run):
	fname=filename(team,run)
	if not os.path.isdir(team):
		raise IOError("No such team")
	if not os.path.isfile(fname):
		raise IOError("No such run")

readRun("ibots",1)
