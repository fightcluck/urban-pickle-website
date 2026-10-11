"""Booking — redirect to Courtsite for availability and reservations."""

from flask import Blueprint, redirect

from app.content import COURTSITE_BOOKING

booking_bp = Blueprint("booking", __name__)


@booking_bp.route("/booking")
def booking():
    return redirect(COURTSITE_BOOKING, code=302)
