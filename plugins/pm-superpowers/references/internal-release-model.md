# Internal Release Model

Use this reference when explaining how PM Superpowers is released to an internal team.

## Recommended Model

Publish PM Superpowers as a project or team marketplace:

- Plugin source: `plugins/pm-superpowers`
- Marketplace file: `.agents/plugins/marketplace.json`
- Marketplace name: `pm-superpowers-internal`
- Marketplace source path for the plugin: `./plugins/pm-superpowers`

This keeps the plugin close to the team's product operating system and allows versioned review through normal repository changes.

## Relationship To Existing PM Skills

The existing 68 PM skills should be distributed as the team's PM method library. PM Superpowers should depend on that library operationally, not copy it:

- Keep `pm-skills` installed as the bottom-layer method plugin set.
- Keep PM Superpowers as the workflow orchestration plugin.
- When a new PM method is needed, add it to the PM skills library if it is an atomic method.
- When a new scenario or governance rule is needed, add it to PM Superpowers.

## Internal Installation Flow

For each team member:

1. Install the existing PM skills marketplace or plugin set used by the team.
2. Add the internal PM Superpowers marketplace.
3. Install `pm-superpowers` from that marketplace.
4. Start a new Codex thread so the newly installed skills are loaded.

Example commands:

```bash
codex plugin marketplace add <internal-repo-url-or-local-path>
codex plugin add pm-superpowers@pm-superpowers-internal
```

If the marketplace is a local checkout:

```bash
codex plugin marketplace add /path/to/product-repo
codex plugin add pm-superpowers@pm-superpowers-internal
```

## Release Workflow

1. Update skills, references, templates, or docs.
2. Run plugin validation and skill validation.
3. Bump the plugin version when shipping to the team.
4. Commit and push the repository.
5. Ask users to update or reinstall the plugin from the internal marketplace.
6. Announce changes with affected workflows, new gates, and migration notes.

## Versioning

- Patch version: wording, templates, docs, or low-risk gates.
- Minor version: new workflow skill, new scene, or new downstream handoff contract.
- Major version: breaking change to workflow outputs or team operating standards.

## Rollout Recommendation

Start with `AVAILABLE`, not `INSTALLED_BY_DEFAULT`, until the team confirms the workflows. Move to default install after pilot feedback from new PMs, experienced PMs, design, and engineering.
