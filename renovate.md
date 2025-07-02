# Renovate Configuration

This project uses [Renovate](https://docs.renovatebot.com/) to keep dependencies up to date automatically.

Below is a quick explanation of the configuration settings.

## Main keys and their purpose

* **extends**
  Inherits the default recommended Renovate settings (`config:base`).

* **timezone**
  Sets the timezone used for scheduling updates (`America/Toronto`).

* **schedule**
  Limits when Renovate is allowed to create or update pull requests.
  Example: only on weekdays between 9am and 5pm.

* **dependencyDashboard**
  Enables a GitHub issue that summarizes all available dependency updates.

* **automerge**
  Allows Renovate to automatically merge pull requests when possible.

* **automergeType**
  Specifies how automerge works.
  `"pr"` means merge the pull request after CI tests pass.

* **rebaseWhen**
  Rebase pull requests when the base branch changes (e.g. when `main` is updated).

* **labels**
  Adds custom labels to Renovate pull requests.
  Example: `"dependencies"`.

* **packageRules**
  Defines special rules for certain packages:

  * Automatically merge only minor and patch updates.
  * Group ESLint and Prettier updates into a single pull request with the label `"dev"`.
  * Disable updates for Dockerfiles.

---

This configuration helps keep the project secure and up to date, with minimal manual work.
