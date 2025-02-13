from __future__ import annotations

import ckan.plugins.toolkit as tk
import ckan.types as types
from flask import Blueprint, Response
from flask.views import MethodView

from ckanext.ap_main.utils import ap_before_request

tour = Blueprint("tour", __name__)
tour.before_request(ap_before_request)


class TourUpdateView(MethodView):
    def get(self, tour_id: str) -> str:
        try:
            tour = tk.get_action("tour_show")(self._build_context(), {"id": tour_id})
        except tk.ValidationError:
            return tk.render("tour/tour_404.html")

        return tk.render("tour/tour_edit.html", extra_vars={"data": tour, "errors": {}})

    def post(self, tour_id: str) -> Response | str:
        try:
            tour = tk.get_action("tour_show")(self._build_context(), {"id": tour_id})
        except tk.ValidationError:
            return tk.render("tour/tour_404.html")

        data_dict = self._prepare_payload(tour_id)

        try:
            tk.get_action("tour_update")(self._build_context(), data_dict)
        except tk.ValidationError as e:
            return tk.render(
                "tour/tour_edit.html",
                extra_vars={
                    "data": tour,
                    "errors": e.error_dict,
                    "error_summary": e.error_summary,
                },
            )

        tk.h.flash_success(tk._("The tour has been updated!"))

        return tk.redirect_to("tour.list")

    def _build_context(self) -> types.Context:
        return {
            "user": tk.current_user.name,  # type: ignore
            "auth_user_obj": tk.current_user,
        }

    def _prepare_payload(self, tour_id: str):
        step_fields = (
            "step_id",
            "step_title",
            "step_element",
            "step_intro",
            "step_position",
            "step_clear",
            "step_index",
        )

        steps = {}

        for field_name in step_fields:
            _, field = field_name.split("_")

            for idx, value in enumerate(tk.request.form.getlist(field_name), start=1):
                steps.setdefault(idx, {})
                steps[idx][field] = value

        for idx, url in enumerate(tk.request.form.getlist("step_url"), start=1):
            if not url:
                continue

            steps[idx].setdefault("image", [{}])
            steps[idx]["image"][0].update({"url": url or None})

        for idx, file in enumerate(tk.request.files.getlist("step_upload"), start=1):
            if not file:
                continue

            # remove url from payload, because we are uploading a file instead
            steps[idx]["image"][0].pop("url", None)
            steps[idx].setdefault("image", [{}])
            steps[idx]["image"][0].update({"upload": file or None})

        return {
            "id": tour_id,
            "title": tk.request.form.get("title"),
            "anchor": tk.request.form.get("anchor"),
            "page": tk.request.form.get("page"),
            "steps": [step for step in steps.values()],
        }
