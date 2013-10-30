alias sup='supervisorctl -c /home/...'
alias svnjoin="egrep ^M| awk '{print \$2}' | xargs"

function get_ts () { echo `date --date="@$1"`; }
alias myts=get_ts

function find_and_commit () { svn ci `svn st $@ | egrep '^(M|D|A)' | awk '{print \$NF}' | xargs`; }
alias ci=find_and_commit
