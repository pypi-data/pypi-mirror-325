use std::sync::{Arc, RwLock};

use crate::{Referable, Schemas};

use super::ValueSchema;

#[derive(Debug, Default, Clone)]
pub struct AllOfSchema {
    pub title: Option<String>,
    pub description: Option<String>,
    pub schemas: Schemas,
    pub default: Option<serde_json::Value>,
}

impl AllOfSchema {
    pub fn new(object: &serde_json::Map<String, serde_json::Value>) -> Self {
        let title = object
            .get("title")
            .and_then(|v| v.as_str())
            .map(|s| s.to_string());
        let description = object
            .get("description")
            .and_then(|v| v.as_str())
            .map(|s| s.to_string());
        let schemas = object
            .get("allOf")
            .and_then(|v| v.as_array())
            .map(|a| {
                a.iter()
                    .filter_map(|v| v.as_object())
                    .filter_map(Referable::<ValueSchema>::new)
                    .collect()
            })
            .unwrap_or_default();
        let default = object.get("default").cloned();

        Self {
            title,
            description,
            schemas: Arc::new(RwLock::new(schemas)),
            default,
        }
    }

    pub fn value_type(&self) -> crate::ValueType {
        crate::ValueType::AllOf(
            self.schemas
                .read()
                .unwrap()
                .iter()
                .map(|schema| schema.value_type())
                .collect(),
        )
    }
}
