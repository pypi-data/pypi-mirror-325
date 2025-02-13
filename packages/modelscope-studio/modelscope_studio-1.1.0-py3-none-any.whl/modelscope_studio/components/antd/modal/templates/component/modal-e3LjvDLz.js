import { i as de, a as W, r as fe, g as me, w as P, b as _e } from "./Index-BzU1kQLw.js";
const C = window.ms_globals.React, se = window.ms_globals.React.forwardRef, le = window.ms_globals.React.useRef, ce = window.ms_globals.React.useState, ae = window.ms_globals.React.useEffect, ue = window.ms_globals.React.useMemo, N = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, U = window.ms_globals.internalContext.ContextPropsProvider, he = window.ms_globals.antd.Modal;
var ge = /\s/;
function be(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var xe = /^\s+/;
function we(e) {
  return e && e.slice(0, be(e) + 1).replace(xe, "");
}
var z = NaN, ye = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, ve = parseInt;
function G(e) {
  if (typeof e == "number")
    return e;
  if (de(e))
    return z;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = we(e);
  var o = Ce.test(e);
  return o || Ee.test(e) ? ve(e.slice(2), o ? 2 : 8) : ye.test(e) ? z : +e;
}
var F = function() {
  return fe.Date.now();
}, Ie = "Expected a function", Re = Math.max, ke = Math.min;
function Se(e, t, o) {
  var s, i, n, r, l, u, _ = 0, p = !1, c = !1, h = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = G(t) || 0, W(o) && (p = !!o.leading, c = "maxWait" in o, n = c ? Re(G(o.maxWait) || 0, t) : n, h = "trailing" in o ? !!o.trailing : h);
  function d(f) {
    var w = s, S = i;
    return s = i = void 0, _ = f, r = e.apply(S, w), r;
  }
  function E(f) {
    return _ = f, l = setTimeout(b, t), p ? d(f) : r;
  }
  function m(f) {
    var w = f - u, S = f - _, D = t - w;
    return c ? ke(D, n - S) : D;
  }
  function g(f) {
    var w = f - u, S = f - _;
    return u === void 0 || w >= t || w < 0 || c && S >= n;
  }
  function b() {
    var f = F();
    if (g(f))
      return v(f);
    l = setTimeout(b, m(f));
  }
  function v(f) {
    return l = void 0, h && s ? d(f) : (s = i = void 0, r);
  }
  function I() {
    l !== void 0 && clearTimeout(l), _ = 0, s = u = i = l = void 0;
  }
  function a() {
    return l === void 0 ? r : v(F());
  }
  function R() {
    var f = F(), w = g(f);
    if (s = arguments, i = this, u = f, w) {
      if (l === void 0)
        return E(u);
      if (c)
        return clearTimeout(l), l = setTimeout(b, t), d(u);
    }
    return l === void 0 && (l = setTimeout(b, t)), r;
  }
  return R.cancel = I, R.flush = a, R;
}
var ee = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Te = C, Pe = Symbol.for("react.element"), Oe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = Te.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Fe = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function te(e, t, o) {
  var s, i = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (s in t) je.call(t, s) && !Fe.hasOwnProperty(s) && (i[s] = t[s]);
  if (e && e.defaultProps) for (s in t = e.defaultProps, t) i[s] === void 0 && (i[s] = t[s]);
  return {
    $$typeof: Pe,
    type: e,
    key: n,
    ref: r,
    props: i,
    _owner: Le.current
  };
}
L.Fragment = Oe;
L.jsx = te;
L.jsxs = te;
ee.exports = L;
var x = ee.exports;
const {
  SvelteComponent: Be,
  assign: H,
  binding_callbacks: K,
  check_outros: Ne,
  children: ne,
  claim_element: re,
  claim_space: We,
  component_subscribe: q,
  compute_slots: Ae,
  create_slot: Me,
  detach: k,
  element: oe,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: De,
  get_slot_changes: Ue,
  group_outros: ze,
  init: Ge,
  insert_hydration: O,
  safe_not_equal: He,
  set_custom_element_data: ie,
  space: Ke,
  transition_in: j,
  transition_out: A,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function X(e) {
  let t, o;
  const s = (
    /*#slots*/
    e[7].default
  ), i = Me(
    s,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = oe("svelte-slot"), i && i.c(), this.h();
    },
    l(n) {
      t = re(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ne(t);
      i && i.l(r), r.forEach(k), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, t, r), i && i.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      i && i.p && (!o || r & /*$$scope*/
      64) && qe(
        i,
        s,
        n,
        /*$$scope*/
        n[6],
        o ? Ue(
          s,
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
      o || (j(i, n), o = !0);
    },
    o(n) {
      A(i, n), o = !1;
    },
    d(n) {
      n && k(t), i && i.d(n), e[9](null);
    }
  };
}
function Qe(e) {
  let t, o, s, i, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = oe("react-portal-target"), o = Ke(), n && n.c(), s = V(), this.h();
    },
    l(r) {
      t = re(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ne(t).forEach(k), o = We(r), n && n.l(r), s = V(), this.h();
    },
    h() {
      ie(t, "class", "svelte-1rt0kpf");
    },
    m(r, l) {
      O(r, t, l), e[8](t), O(r, o, l), n && n.m(r, l), O(r, s, l), i = !0;
    },
    p(r, [l]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, l), l & /*$$slots*/
      16 && j(n, 1)) : (n = X(r), n.c(), j(n, 1), n.m(s.parentNode, s)) : n && (ze(), A(n, 1, 1, () => {
        n = null;
      }), Ne());
    },
    i(r) {
      i || (j(n), i = !0);
    },
    o(r) {
      A(n), i = !1;
    },
    d(r) {
      r && (k(t), k(o), k(s)), e[8](null), n && n.d(r);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ze(e, t, o) {
  let s, i, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const l = Ae(n);
  let {
    svelteInit: u
  } = t;
  const _ = P(Y(t)), p = P();
  q(e, p, (a) => o(0, s = a));
  const c = P();
  q(e, c, (a) => o(1, i = a));
  const h = [], d = Je("$$ms-gr-react-wrapper"), {
    slotKey: E,
    slotIndex: m,
    subSlotIndex: g
  } = me() || {}, b = u({
    parent: d,
    props: _,
    target: p,
    slot: c,
    slotKey: E,
    slotIndex: m,
    subSlotIndex: g,
    onDestroy(a) {
      h.push(a);
    }
  });
  Ye("$$ms-gr-react-wrapper", b), Ve(() => {
    _.set(Y(t));
  }), Xe(() => {
    h.forEach((a) => a());
  });
  function v(a) {
    K[a ? "unshift" : "push"](() => {
      s = a, p.set(s);
    });
  }
  function I(a) {
    K[a ? "unshift" : "push"](() => {
      i = a, c.set(i);
    });
  }
  return e.$$set = (a) => {
    o(17, t = H(H({}, t), J(a))), "svelteInit" in a && o(5, u = a.svelteInit), "$$scope" in a && o(6, r = a.$$scope);
  }, t = J(t), [s, i, p, c, l, u, r, n, v, I];
}
class $e extends Be {
  constructor(t) {
    super(), Ge(this, t, Ze, Qe, He, {
      svelteInit: 5
    });
  }
}
const Q = window.ms_globals.rerender, B = window.ms_globals.tree;
function et(e, t = {}) {
  function o(s) {
    const i = P(), n = new $e({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const l = {
            key: window.ms_globals.autokey,
            svelteInstance: i,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, u = r.parent ?? B;
          return u.nodes = [...u.nodes, l], Q({
            createPortal: N,
            node: B
          }), r.onDestroy(() => {
            u.nodes = u.nodes.filter((_) => _.svelteInstance !== i), Q({
              createPortal: N,
              node: B
            });
          }), l;
        },
        ...s.props
      }
    });
    return i.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(o);
    });
  });
}
const tt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function nt(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const s = e[o];
    return t[o] = rt(o, s), t;
  }, {}) : {};
}
function rt(e, t) {
  return typeof t == "number" && !tt.includes(e) ? t + "px" : t;
}
function M(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const i = C.Children.toArray(e._reactElement.props.children).map((n) => {
      if (C.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: l
        } = M(n.props.el);
        return C.cloneElement(n, {
          ...n.props,
          el: l,
          children: [...C.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return i.originalChildren = e._reactElement.props.children, t.push(N(C.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: i
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((i) => {
    e.getEventListeners(i).forEach(({
      listener: r,
      type: l,
      useCapture: u
    }) => {
      o.addEventListener(l, r, u);
    });
  });
  const s = Array.from(e.childNodes);
  for (let i = 0; i < s.length; i++) {
    const n = s[i];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: l
      } = M(n);
      t.push(...l), o.appendChild(r);
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
const y = se(({
  slot: e,
  clone: t,
  className: o,
  style: s,
  observeAttributes: i
}, n) => {
  const r = le(), [l, u] = ce([]), {
    forceClone: _
  } = pe(), p = _ ? !0 : t;
  return ae(() => {
    var E;
    if (!r.current || !e)
      return;
    let c = e;
    function h() {
      let m = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (m = c.children[0], m.tagName.toLowerCase() === "react-portal-target" && m.children[0] && (m = m.children[0])), ot(n, m), o && m.classList.add(...o.split(" ")), s) {
        const g = nt(s);
        Object.keys(g).forEach((b) => {
          m.style[b] = g[b];
        });
      }
    }
    let d = null;
    if (p && window.MutationObserver) {
      let m = function() {
        var I, a, R;
        (I = r.current) != null && I.contains(c) && ((a = r.current) == null || a.removeChild(c));
        const {
          portals: b,
          clonedElement: v
        } = M(e);
        c = v, u(b), c.style.display = "contents", h(), (R = r.current) == null || R.appendChild(c);
      };
      m();
      const g = Se(() => {
        m(), d == null || d.disconnect(), d == null || d.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: i
        });
      }, 50);
      d = new window.MutationObserver(g), d.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", h(), (E = r.current) == null || E.appendChild(c);
    return () => {
      var m, g;
      c.style.display = "", (m = r.current) != null && m.contains(c) && ((g = r.current) == null || g.removeChild(c)), d == null || d.disconnect();
    };
  }, [e, p, o, s, n, i]), C.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...l);
});
function it(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function st(e, t = !1) {
  try {
    if (_e(e))
      return e;
    if (t && !it(e))
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
function T(e, t) {
  return ue(() => st(e, t), [e, t]);
}
function Z(e, t) {
  return e ? /* @__PURE__ */ x.jsx(y, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function $({
  key: e,
  slots: t,
  targets: o
}, s) {
  return t[e] ? (...i) => o ? o.map((n, r) => /* @__PURE__ */ x.jsx(U, {
    params: i,
    forceClone: !0,
    children: Z(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ x.jsx(U, {
    params: i,
    forceClone: !0,
    children: Z(t[e], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const ct = et(({
  slots: e,
  afterClose: t,
  afterOpenChange: o,
  getContainer: s,
  children: i,
  modalRender: n,
  setSlotParams: r,
  ...l
}) => {
  var h, d;
  const u = T(o), _ = T(t), p = T(s), c = T(n);
  return /* @__PURE__ */ x.jsx(he, {
    ...l,
    afterOpenChange: u,
    afterClose: _,
    okText: e.okText ? /* @__PURE__ */ x.jsx(y, {
      slot: e.okText
    }) : l.okText,
    okButtonProps: {
      ...l.okButtonProps || {},
      icon: e["okButtonProps.icon"] ? /* @__PURE__ */ x.jsx(y, {
        slot: e["okButtonProps.icon"]
      }) : (h = l.okButtonProps) == null ? void 0 : h.icon
    },
    cancelText: e.cancelText ? /* @__PURE__ */ x.jsx(y, {
      slot: e.cancelText
    }) : l.cancelText,
    cancelButtonProps: {
      ...l.cancelButtonProps || {},
      icon: e["cancelButtonProps.icon"] ? /* @__PURE__ */ x.jsx(y, {
        slot: e["cancelButtonProps.icon"]
      }) : (d = l.cancelButtonProps) == null ? void 0 : d.icon
    },
    closable: e["closable.closeIcon"] ? {
      ...typeof l.closable == "object" ? l.closable : {},
      closeIcon: /* @__PURE__ */ x.jsx(y, {
        slot: e["closable.closeIcon"]
      })
    } : l.closable,
    closeIcon: e.closeIcon ? /* @__PURE__ */ x.jsx(y, {
      slot: e.closeIcon
    }) : l.closeIcon,
    footer: e.footer ? $({
      slots: e,
      setSlotParams: r,
      key: "footer"
    }) : l.footer,
    title: e.title ? /* @__PURE__ */ x.jsx(y, {
      slot: e.title
    }) : l.title,
    modalRender: e.modalRender ? $({
      slots: e,
      setSlotParams: r,
      key: "modalRender"
    }) : c,
    getContainer: typeof s == "string" ? p : s,
    children: i
  });
});
export {
  ct as Modal,
  ct as default
};
