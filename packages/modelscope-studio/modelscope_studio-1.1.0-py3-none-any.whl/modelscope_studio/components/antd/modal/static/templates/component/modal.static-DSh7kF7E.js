import { i as de, a as N, r as fe, g as me, w as k, b as _e } from "./Index-Rr2i1D7c.js";
const R = window.ms_globals.React, ce = window.ms_globals.React.forwardRef, ee = window.ms_globals.React.useRef, ae = window.ms_globals.React.useState, te = window.ms_globals.React.useEffect, ue = window.ms_globals.React.useMemo, M = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, U = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Modal;
var ge = /\s/;
function xe(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var ye = /^\s+/;
function we(e) {
  return e && e.slice(0, xe(e) + 1).replace(ye, "");
}
var H = NaN, be = /^[-+]0x[0-9a-f]+$/i, Ee = /^0b[01]+$/i, ve = /^0o[0-7]+$/i, Ce = parseInt;
function z(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return H;
  if (N(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = N(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var o = Ee.test(e);
  return o || ve.test(e) ? Ce(e.slice(2), o ? 2 : 8) : be.test(e) ? H : +e;
}
var L = function() {
  return fe.Date.now();
}, Ie = "Expected a function", Re = Math.max, Se = Math.min;
function Te(e, t, o) {
  var l, s, n, r, i, d, p = 0, g = !1, c = !1, u = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = z(t) || 0, N(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Re(z(o.maxWait) || 0, t) : n, u = "trailing" in o ? !!o.trailing : u);
  function _(f) {
    var w = l, T = s;
    return l = s = void 0, p = f, r = e.apply(T, w), r;
  }
  function v(f) {
    return p = f, i = setTimeout(x, t), g ? _(f) : r;
  }
  function m(f) {
    var w = f - d, T = f - p, D = t - w;
    return c ? Se(D, n - T) : D;
  }
  function h(f) {
    var w = f - d, T = f - p;
    return d === void 0 || w >= t || w < 0 || c && T >= n;
  }
  function x() {
    var f = L();
    if (h(f))
      return C(f);
    i = setTimeout(x, m(f));
  }
  function C(f) {
    return i = void 0, u && l ? _(f) : (l = s = void 0, r);
  }
  function b() {
    i !== void 0 && clearTimeout(i), p = 0, l = d = s = i = void 0;
  }
  function a() {
    return i === void 0 ? r : C(L());
  }
  function E() {
    var f = L(), w = h(f);
    if (l = arguments, s = this, d = f, w) {
      if (i === void 0)
        return v(d);
      if (c)
        return clearTimeout(i), i = setTimeout(x, t), _(d);
    }
    return i === void 0 && (i = setTimeout(x, t)), r;
  }
  return E.cancel = b, E.flush = a, E;
}
var ne = {
  exports: {}
}, F = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Pe = R, ke = Symbol.for("react.element"), Oe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Fe = Pe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function re(e, t, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) je.call(t, l) && !Le.hasOwnProperty(l) && (s[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) s[l] === void 0 && (s[l] = t[l]);
  return {
    $$typeof: ke,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Fe.current
  };
}
F.Fragment = Oe;
F.jsx = re;
F.jsxs = re;
ne.exports = F;
var y = ne.exports;
const {
  SvelteComponent: Be,
  assign: G,
  binding_callbacks: K,
  check_outros: Me,
  children: oe,
  claim_element: se,
  claim_space: Ne,
  component_subscribe: q,
  compute_slots: Ae,
  create_slot: We,
  detach: S,
  element: le,
  empty: J,
  exclude_internal_props: X,
  get_all_dirty_from_scope: De,
  get_slot_changes: Ue,
  group_outros: He,
  init: ze,
  insert_hydration: O,
  safe_not_equal: Ge,
  set_custom_element_data: ie,
  space: Ke,
  transition_in: j,
  transition_out: A,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Qe
} = window.__gradio__svelte__internal;
function Y(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = We(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = le("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = se(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = oe(t);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && qe(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? Ue(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : De(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (j(s, n), o = !0);
    },
    o(n) {
      A(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function Ze(e) {
  let t, o, l, s, n = (
    /*$$slots*/
    e[4].default && Y(e)
  );
  return {
    c() {
      t = le("react-portal-target"), o = Ke(), n && n.c(), l = J(), this.h();
    },
    l(r) {
      t = se(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), oe(t).forEach(S), o = Ne(r), n && n.l(r), l = J(), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, t, i), e[8](t), O(r, o, i), n && n.m(r, i), O(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && j(n, 1)) : (n = Y(r), n.c(), j(n, 1), n.m(l.parentNode, l)) : n && (He(), A(n, 1, 1, () => {
        n = null;
      }), Me());
    },
    i(r) {
      s || (j(n), s = !0);
    },
    o(r) {
      A(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(l)), e[8](null), n && n.d(r);
    }
  };
}
function Q(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ve(e, t, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = Ae(n);
  let {
    svelteInit: d
  } = t;
  const p = k(Q(t)), g = k();
  q(e, g, (a) => o(0, l = a));
  const c = k();
  q(e, c, (a) => o(1, s = a));
  const u = [], _ = Xe("$$ms-gr-react-wrapper"), {
    slotKey: v,
    slotIndex: m,
    subSlotIndex: h
  } = me() || {}, x = d({
    parent: _,
    props: p,
    target: g,
    slot: c,
    slotKey: v,
    slotIndex: m,
    subSlotIndex: h,
    onDestroy(a) {
      u.push(a);
    }
  });
  Qe("$$ms-gr-react-wrapper", x), Je(() => {
    p.set(Q(t));
  }), Ye(() => {
    u.forEach((a) => a());
  });
  function C(a) {
    K[a ? "unshift" : "push"](() => {
      l = a, g.set(l);
    });
  }
  function b(a) {
    K[a ? "unshift" : "push"](() => {
      s = a, c.set(s);
    });
  }
  return e.$$set = (a) => {
    o(17, t = G(G({}, t), X(a))), "svelteInit" in a && o(5, d = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = X(t), [l, s, g, c, i, d, r, n, C, b];
}
class $e extends Be {
  constructor(t) {
    super(), ze(this, t, Ve, Ze, Ge, {
      svelteInit: 5
    });
  }
}
const Z = window.ms_globals.rerender, B = window.ms_globals.tree;
function et(e, t = {}) {
  function o(l) {
    const s = k(), n = new $e({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, d = r.parent ?? B;
          return d.nodes = [...d.nodes, i], Z({
            createPortal: M,
            node: B
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((p) => p.svelteInstance !== s), Z({
              createPortal: M,
              node: B
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return t[o] = rt(o, l), t;
  }, {}) : {};
}
function rt(e, t) {
  return typeof t == "number" && !tt.includes(e) ? t + "px" : t;
}
function W(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = R.Children.toArray(e._reactElement.props.children).map((n) => {
      if (R.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = W(n.props.el);
        return R.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...R.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(M(R.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: d
    }) => {
      o.addEventListener(i, r, d);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = W(n);
      t.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function ot(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const I = ce(({
  slot: e,
  clone: t,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = ee(), [i, d] = ae([]), {
    forceClone: p
  } = pe(), g = p ? !0 : t;
  return te(() => {
    var v;
    if (!r.current || !e)
      return;
    let c = e;
    function u() {
      let m = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (m = c.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), ot(n, m), o && m.classList.add(...o.split(" ")), l) {
        const h = nt(l);
        Object.keys(h).forEach((x) => {
          m.style[x] = h[x];
        });
      }
    }
    let _ = null;
    if (g && window.MutationObserver) {
      let m = function() {
        var b, a, E;
        (b = r.current) != null && b.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: x,
          clonedElement: C
        } = W(e);
        c = C, d(x), c.style.display = "contents", u(), (E = r.current) == null || E.appendChild(c);
      };
      m();
      const h = Te(() => {
        m(), _ == null || _.disconnect(), _ == null || _.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      _ = new window.MutationObserver(h), _.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", u(), (v = r.current) == null || v.appendChild(c);
    return () => {
      var m, h;
      c.style.display = "", (m = r.current) != null && m.contains(c) && ((h = r.current) == null || h.removeChild(c)), _ == null || _.disconnect();
    };
  }, [e, g, o, l, n, s]), R.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function st(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function lt(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !st(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function P(e, t) {
  return ue(() => lt(e, t), [e, t]);
}
function V(e, t) {
  return e ? /* @__PURE__ */ y.jsx(I, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function $({
  key: e,
  slots: t,
  targets: o
}, l) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ y.jsx(U, {
    params: s,
    forceClone: !0,
    children: V(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ y.jsx(U, {
    params: s,
    forceClone: !0,
    children: V(t[e], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const ct = et(({
  slots: e,
  afterClose: t,
  afterOpenChange: o,
  getContainer: l,
  children: s,
  modalRender: n,
  setSlotParams: r,
  onVisible: i,
  onCancel: d,
  onOk: p,
  visible: g,
  type: c,
  ...u
}) => {
  const _ = P(o), v = P(t), m = P(l), h = P(n), [x, C] = he.useModal(), b = ee(null);
  return te(() => {
    var a, E, f;
    g ? b.current = x[c || "info"]({
      ...u,
      autoFocusButton: u.autoFocusButton === void 0 ? null : u.autoFocusButton,
      afterOpenChange: _,
      afterClose: v,
      getContainer: typeof l == "string" ? m : l,
      okText: e.okText ? /* @__PURE__ */ y.jsx(I, {
        slot: e.okText
      }) : u.okText,
      okButtonProps: {
        ...u.okButtonProps || {},
        icon: e["okButtonProps.icon"] ? /* @__PURE__ */ y.jsx(I, {
          slot: e["okButtonProps.icon"]
        }) : (a = u.okButtonProps) == null ? void 0 : a.icon
      },
      cancelText: e.cancelText ? /* @__PURE__ */ y.jsx(I, {
        slot: e.cancelText
      }) : u.cancelText,
      cancelButtonProps: {
        ...u.cancelButtonProps || {},
        icon: e["cancelButtonProps.icon"] ? /* @__PURE__ */ y.jsx(I, {
          slot: e["cancelButtonProps.icon"]
        }) : (E = u.cancelButtonProps) == null ? void 0 : E.icon
      },
      closable: e["closable.closeIcon"] ? {
        ...typeof u.closable == "object" ? u.closable : {},
        closeIcon: /* @__PURE__ */ y.jsx(I, {
          slot: e["closable.closeIcon"]
        })
      } : u.closable,
      closeIcon: e.closeIcon ? /* @__PURE__ */ y.jsx(I, {
        slot: e.closeIcon
      }) : u.closeIcon,
      footer: e.footer ? $({
        slots: e,
        setSlotParams: r,
        key: "footer"
      }) : u.footer,
      title: e.title ? /* @__PURE__ */ y.jsx(I, {
        slot: e.title
      }) : u.title,
      modalRender: e.modalRender ? $({
        slots: e,
        setSlotParams: r,
        key: "modalRender"
      }) : h,
      onCancel(...w) {
        d == null || d(...w), i == null || i(!1);
      },
      onOk(...w) {
        p == null || p(...w), i == null || i(!1);
      }
    }) : ((f = b.current) == null || f.destroy(), b.current = null);
  }, [g]), /* @__PURE__ */ y.jsxs(y.Fragment, {
    children: [/* @__PURE__ */ y.jsx("div", {
      style: {
        display: "none"
      },
      children: s
    }), C]
  });
});
export {
  ct as ModalStatic,
  ct as default
};
