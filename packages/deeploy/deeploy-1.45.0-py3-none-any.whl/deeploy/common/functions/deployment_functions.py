def validate_temporary_s3_credentials(values) -> None:
    model_temp_s3_credentials = [
        "model_s3_temporary_access_key_id",
        "model_s3_temporary_secret_access_key",
        "model_s3_temporary_session_token",
    ]
    has_any_model_temp_s3_credentials = any(
        values.get(attr) is not None for attr in model_temp_s3_credentials
    )
    has_all_model_temp_s3_credentials = all(
        values.get(attr) is not None for attr in model_temp_s3_credentials
    )

    if has_any_model_temp_s3_credentials and not has_all_model_temp_s3_credentials:
        raise ValueError(
            f"If one attribute for the models temporary S3 credentials is set, all of {', '.join(model_temp_s3_credentials)} must be set."
        )

    explainer_temp_s3_credentials = [
        "explainer_s3_temporary_access_key_id",
        "explainer_s3_temporary_secret_access_key",
        "explainer_s3_temporary_session_token",
    ]
    has_any_explainer_temp_s3_credentials = any(
        values.get(attr) is not None for attr in explainer_temp_s3_credentials
    )
    has_all_explainer_temp_s3_credentials = all(
        values.get(attr) is not None for attr in explainer_temp_s3_credentials
    )

    if has_any_explainer_temp_s3_credentials and not has_all_explainer_temp_s3_credentials:
        raise ValueError(
            f"If one attribute for the explainers temporary S3 credentials is set, all of {', '.join(explainer_temp_s3_credentials)} must be set."
        )


def validate_temporary_azure_credentials(values) -> None:
    model_temp_azure_credentials = [
        "model_azure_temporary_sas_token",
        "model_azure_temporary_storage_account",
    ]
    has_any_model_temp_azure_credentials = any(
        values.get(attr) is not None for attr in model_temp_azure_credentials
    )
    has_all_model_temp_azure_credentials = all(
        values.get(attr) is not None for attr in model_temp_azure_credentials
    )

    if has_any_model_temp_azure_credentials and not has_all_model_temp_azure_credentials:
        raise ValueError(
            f"If one attribute for the models temporary Azure credentials is set, all of {', '.join(model_temp_azure_credentials)} must be set."
        )

    explainer_temp_azure_credentials = [
        "explainer_azure_temporary_sas_token",
        "explainer_azure_temporary_storage_account",
    ]
    has_any_explainer_temp_azure_credentials = any(
        values.get(attr) is not None for attr in explainer_temp_azure_credentials
    )
    has_all_explainer_temp_azure_credentials = all(
        values.get(attr) is not None for attr in explainer_temp_azure_credentials
    )

    if has_any_explainer_temp_azure_credentials and not has_all_explainer_temp_azure_credentials:
        raise ValueError(
            f"If one attribute for the explainers temporary Azure credentials is set, all of {', '.join(explainer_temp_azure_credentials)} must be set."
        )
