import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

// These scripts replay archived judgments; they are not reusable judges.
const INPUTS = {
  pass1: {
    'blind_review.csv': '22949d6ffe74ffe49bc7ad8ee386d468df285468189d204dfb176f19b09fd50d',
    'blind_key.json': '1b705485c07f950e8c1f48d146935791ed53f318a652f3e73731de646abec4e2',
  },
  pass2: {
    'blind_review_pass2_blank.csv': '931c50f1ab71a86e544cc4b91fff4386f70061be473e8a11da43f978092cd16e',
    'blind_key_pass2.json': 'c8c087a4a7ce1b03e3deedc2c2ef0f811b8ae2c111ceb3be1bfc25f0e8a34846',
  },
};

export function assertArchivedMainReview(runDir, pass) {
  if (!INPUTS[pass]) throw new Error(`Unknown archived review pass: ${pass}`);
  const manifest = JSON.parse(fs.readFileSync(path.join(runDir, 'manifest.json'), 'utf8'));
  if (manifest.run_id !== 'main72_v3_2026-09-03T07-35-49-603Z') {
    throw new Error('ARCHIVED_REVIEW_ONLY: new runs require fresh semantic judgments');
  }
  for (const [name, expected] of Object.entries(INPUTS[pass])) {
    const actual = crypto.createHash('sha256').update(fs.readFileSync(path.join(runDir, name))).digest('hex');
    if (actual !== expected) throw new Error(`ARCHIVED_REVIEW_INPUT_MISMATCH: ${name}`);
  }
}
