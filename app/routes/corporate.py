"""Corporate packages and contact routes."""

from flask import Blueprint, flash, redirect, render_template, request, url_for

corporate_bp = Blueprint("corporate", __name__)


@corporate_bp.route("/corporate", methods=["GET", "POST"])
def corporate():
    if request.method == "POST":
        flash(
            "Thanks — email wiring is coming soon. For a faster reply, WhatsApp us.",
            "info",
        )
        return redirect(url_for("corporate.corporate"))
    return render_template("corporate.html")
