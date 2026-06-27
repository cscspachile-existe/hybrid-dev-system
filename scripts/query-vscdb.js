const Database = require('better-sqlite3');
const db = new Database(process.argv[2], { readonly: true });
const rows = db.prepare(
  "SELECT key, length(value) as len FROM ItemTable WHERE key LIKE '%cline%' OR key LIKE '%claude-dev%' OR key LIKE '%saoud%'"
).all();
for (const row of rows) console.log(row.key, row.len);
