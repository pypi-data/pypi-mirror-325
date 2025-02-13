from cr.bitbucket import fetch_pull_requests, fetch_diff, post_comment
from cr.ai_layer import analyze_code_diff

def review_pr():
    """Review all open pull requests."""
    print("Fetching open PRs...")
    pull_requests = fetch_pull_requests()

    if not pull_requests:
        print("No open pull requests found.")
        return

    for pr in pull_requests:
        print(f"Reviewing PR #{pr['id']}: {pr['title']}")
        diff = fetch_diff(pr["id"])
        feedback = analyze_code_diff(diff)
        post_comment(pr["id"], feedback)

if __name__ == "__main__":
    review_pr()